-- Pandoc filter for the Paludal docs (see the Makefile). It runs in three passes:
--
-- 1. HTML only: nest the flat headings into <section>s with stable ids, and wrap each block in
--    <div class="block KIND"> so the "hide notes" toggle can tell tables, decisions and reasons
--    from notes. Sections holding any of those are marked has-table, the rest no-table.
-- 2. Every format: unit symbols. HTML gets <abbr> tooltips naming the unit; every format shows a
--    prefix with Primel's arrows (tqop -> t↑op). LaTeX gets table column widths sized from content.
--    Mermaid diagrams are drawn in HTML, kept as [mermaid] blocks in AsciiDoc, noted in LaTeX.
-- 3. HTML only: build the nav from the sections into the `nav` variable for the template.

local stringify = pandoc.utils.stringify
local is_html = FORMAT:match("html") ~= nil

local function escape(s)
  return (s:gsub("&", "&amp;"):gsub("<", "&lt;"):gsub(">", "&gt;"):gsub('"', "&quot;"))
end

local function render(inlines)
  return pandoc.write(pandoc.Pandoc({ pandoc.Plain(inlines) }), "html5"):gsub("%s+$", "")
end

----------------------------------------------------------------------------------------------
-- Pass 1: sections and blocks

local function slug(text)
  return (text:lower():gsub("[^a-z0-9]+", "-"):gsub("^%-+", ""):gsub("%-+$", ""))
end

local function kind(b)
  if b.t == "Table" then return "table" end
  if b.t == "BulletList" or b.t == "OrderedList" then return "list" end
  if b.t == "CodeBlock" then return b.classes:includes("mermaid") and "diagram" or "code" end
  if b.t == "Para" then
    local first = b.content[1]
    if first and first.t == "Strong" and stringify(first) == "Why:" then return "why" end
    local text = stringify(b)
    if text:find("Decided", 1, true) or text:find("decided)", 1, true) then return "decided" end
  end
  return "para"
end

local MARKS_TABLE = { table = true, diagram = true, decided = true, why = true }

local function wrap(b)
  local k = kind(b)
  if k == "table" then
    b = pandoc.Div({ b }, { class = "table-wrap" })
  elseif k == "diagram" then
    b = pandoc.RawBlock("html", '<pre class="mermaid">' .. escape(b.text) .. "</pre>")
  elseif k == "code" then
    b = pandoc.RawBlock("html", "<pre><code>" .. escape(b.text) .. "</code></pre>")
  end
  return pandoc.Div({ b }, { class = "block " .. k }), MARKS_TABLE[k]
end

local function is_part(sec)
  return sec.level == 1 and stringify(sec.header):match("^Part %d") ~= nil
end

local function to_div(sec)
  local content = { pandoc.Header(sec.level + 1, sec.header.content) }
  for _, b in ipairs(sec.blocks) do content[#content + 1] = b end
  for _, c in ipairs(sec.children) do content[#content + 1] = to_div(c) end
  local classes = { "section", sec.has_table and "has-table" or "no-table" }
  if sec.lead then table.insert(classes, 2, "lead") end
  return pandoc.Div(content, pandoc.Attr(sec.id, classes))
end

local function sections(doc)
  local root = { level = 0, blocks = {}, children = {} }
  local stack = { root }
  for _, b in ipairs(doc.blocks) do
    if b.t == "Header" then
      while stack[#stack].level >= b.level do table.remove(stack) end
      local parent = stack[#stack]
      -- A chapter directly under a Part gets a short id (#prefixes); deeper ones carry their parent's
      local prefix = (parent == root or is_part(parent)) and "" or parent.id .. " "
      local sec = { level = b.level, header = b, blocks = {}, children = {}, has_table = false,
                    id = slug(prefix .. stringify(b)) }
      table.insert(parent.children, sec)
      table.insert(stack, sec)
    else
      local div, marks = wrap(b)
      table.insert(stack[#stack].blocks, div)
      if marks then for _, s in ipairs(stack) do s.has_table = true end end
    end
  end
  if root.children[1] then root.children[1].lead = true end -- the opening section is the intro
  local blocks = { pandoc.Div(root.blocks, { class = "intro" }) }
  for _, s in ipairs(root.children) do blocks[#blocks + 1] = to_div(s) end
  doc.blocks = blocks
  return doc
end

----------------------------------------------------------------------------------------------
-- Pass 2: unit symbols, tables, diagrams

local UNITS = {
  bl = "blink", bt = "beat", br = "breath", ch = "chime", mt = "moment",
  p = "pace", un = "unc", di = "dig", sp = "span", ul = "ulna", ir = "iter", na = "navis", px = "parax",
  li = "lib", cu = "cub", te = "tep",
  vi = "vis", op = "opus", vg = "vig", pr = "pres", ri = "riv", os = "onus",
  im = "imp", gx = "grex", la = "lam", vo = "vox", ag = "ager", tu = "turn",
}
local ROOT_NAMES = { n = "nil", u = "un", b = "bi", t = "tri", q = "quad", p = "pent", h = "hex",
                     s = "sept", o = "oct", e = "enn", d = "dek", l = "el" }
local ROOT_DIGITS = { n = "0", u = "1", b = "2", t = "3", q = "4", p = "5", h = "6",
                      s = "7", o = "8", e = "9", d = "X", l = "E" }
local DEGREE_T = "°t"

local function unit_at(s, i)
  for len = 2, 1, -1 do
    local u = s:sub(i, i + len - 1)
    if #u == len and UNITS[u] and not s:sub(i + len, i + len):match("[%w_]") then return u end
  end
end

-- A symbol found in text: the source text, the name for the tooltip, and the typeset form
local function prefixed(roots, qc, unit)
  local names, digits = {}, {}
  for ch in roots:gmatch(".") do
    names[#names + 1], digits[#digits + 1] = ROOT_NAMES[ch], ROOT_DIGITS[ch]
  end
  local mul = qc == "q"
  return {
    source = roots .. qc .. unit,
    name = ("%s%s-%s (%s 10^%s)"):format(table.concat(names), mul and "qua" or "cia", UNITS[unit],
                                         mul and "×" or "÷", table.concat(digits)),
    shown = roots .. (mul and "↑" or "↓") .. unit,
  }
end

-- Find the symbol starting at byte i of s, if any. `after_digit` / `after_dxe` say the text
-- before s ends in a digit (or X / E) and a space. A prefixed symbol (tqop) is always a unit;
-- a bare one (p, op) only straight after a number or / or ·, so ordinary words are left alone.
local function symbol_at(s, i, after_digit, after_dxe)
  local prev = s:sub(i - 1, i - 1)
  if i == 1 or not prev:match("[%w_]") then
    local run = s:match("^[nubtqphsoedl]+", i)
    if run then
      for k = #run + 1, 2, -1 do -- k is where the q / c sits; c isn't a root, so it may be one past the run
        local qc = s:sub(i + k - 1, i + k - 1)
        if qc == "q" or qc == "c" then
          local u = unit_at(s, i + k)
          if u then return prefixed(run:sub(1, k - 1), qc, u) end
        end
      end
    end
  end
  if (i == 1 and after_digit) or prev:match("[%d/]") or s:sub(i - 2, i - 1) == "·" then
    local u = unit_at(s, i)
    if u then return { source = u, name = UNITS[u], shown = u } end
  end
  if s:sub(i, i + #DEGREE_T - 1) == DEGREE_T and ((i == 1 and after_dxe) or prev:match("[%dXE]")) then
    return { source = DEGREE_T, name = "tep (degrees from freezing)", shown = DEGREE_T }
  end
end

local function symbols(s, after_digit, after_dxe)
  local out, plain, i = {}, 1, 1
  while i <= #s do
    local m = symbol_at(s, i, after_digit, after_dxe)
    if m then
      if i > plain then out[#out + 1] = pandoc.Str(s:sub(plain, i - 1)) end
      out[#out + 1] = is_html
          and pandoc.RawInline("html", ('<abbr title="%s">%s</abbr>'):format(escape(m.name), m.shown))
          or pandoc.Str(m.shown)
      i = i + #m.source
      plain = i
    else
      i = i + 1
    end
  end
  if plain == 1 then return nil end
  if plain <= #s then out[#out + 1] = pandoc.Str(s:sub(plain)) end
  return out
end

local function Inlines(inlines)
  local out = pandoc.Inlines({})
  for i, el in ipairs(inlines) do
    local new
    if el.t == "Str" then
      local before, gap = inlines[i - 2], inlines[i - 1]
      local spaced = gap and (gap.t == "Space" or gap.t == "SoftBreak") and before and before.t == "Str"
      new = symbols(el.text, spaced and before.text:match("%d$") ~= nil,
                    spaced and before.text:match("[%dXE]$") ~= nil)
    end
    if new then out:extend(new) else out:insert(el) end
  end
  return out
end

-- Size LaTeX table columns from their content so wide tables wrap inside the page instead of
-- running off it. Widths are in "characters" against a page of PAGE characters (A4, 2 cm
-- margins, \small tables). A column gets at least its longest word (so numbers never break)
-- and at most CAP characters of its longest cell. Narrow tables keep their natural width;
-- tables that wouldn't fit are scaled to exactly the page width. HTML sizes tables itself.
local PAGE = 100
local CAP = 38

local function measure(s)
  local longest_word, total = 0, utf8.len(s) or #s
  for w in s:gmatch("%S+") do
    local n = utf8.len(w) or #w
    if n > longest_word then longest_word = n end
  end
  return longest_word, total
end

local function Table(tbl)
  local ncols = #tbl.colspecs
  if is_html then
    for i = 1, ncols do tbl.colspecs[i] = { pandoc.AlignDefault } end
    return tbl
  end
  local word, len = {}, {}
  for i = 1, ncols do word[i], len[i] = 3, 3 end
  local function scan(rows)
    for _, row in ipairs(rows) do
      for i, cell in ipairs(row.cells) do
        if i <= ncols then
          local w, l = measure(stringify(cell.contents))
          if w > word[i] then word[i] = w end
          if l > len[i] then len[i] = l end
        end
      end
    end
  end
  scan(tbl.head.rows)
  for _, body in ipairs(tbl.bodies) do scan(body.body) end
  local weight, sum = {}, 0
  for i = 1, ncols do
    weight[i] = math.max(word[i] * 1.2, math.min(len[i], CAP)) + 2.5 -- headers are bold, plus cell padding
    sum = sum + weight[i]
  end
  local scale = math.max(sum, PAGE)
  for i = 1, ncols do tbl.colspecs[i] = { tbl.colspecs[i][1], weight[i] / scale } end
  return tbl
end

local function CodeBlock(cb)
  if not cb.classes:includes("mermaid") then return nil end
  if FORMAT:match("asciidoc") then
    -- asciidoctor-diagram renders [mermaid] blocks directly
    return pandoc.RawBlock("asciidoc", "[mermaid]\n....\n" .. cb.text .. "\n....\n")
  elseif FORMAT:match("latex") then
    return pandoc.Para({ pandoc.Emph({ pandoc.Str("(Diagram - see index.html for the drawn version.)") }) })
  end
end

-- <br> inside a table cell (the prefix matrix) is a line break in every output format
local function RawInline(el)
  if el.format == "html" and el.text:match("^<br%s*/?>$") then return pandoc.LineBreak() end
end

----------------------------------------------------------------------------------------------
-- Pass 3: the nav

local function is_section(b)
  return b.t == "Div" and b.classes:includes("section")
end

local function nav(doc)
  local items = {}
  for _, sec in ipairs(doc.blocks) do
    if is_section(sec) then
      local subs = {}
      for _, c in ipairs(sec.content) do
        if is_section(c) then
          subs[#subs + 1] = ('<li><a href="#%s">%s</a></li>'):format(c.identifier, render(c.content[1].content))
        end
      end
      items[#items + 1] = ('<li class="%s"><a href="#%s">%s</a>%s</li>'):format(
        sec.classes:includes("has-table") and "has-table" or "no-table", sec.identifier,
        render(sec.content[1].content), #subs > 0 and "<ul>" .. table.concat(subs) .. "</ul>" or "")
    end
  end
  doc.meta.nav = pandoc.RawBlock("html", table.concat(items, "\n"))
  return doc
end

----------------------------------------------------------------------------------------------

if is_html then
  return {
    { Pandoc = sections },
    { Inlines = Inlines, Table = Table, RawInline = RawInline },
    { Pandoc = nav },
  }
end
return {
  { Inlines = Inlines, Table = Table, CodeBlock = CodeBlock, RawInline = RawInline },
}
