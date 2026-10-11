## Digits

**Decided:** digits 0 1 2 3 4 5 6 7 8 9 X E (X = dek, ten; E = el, eleven); print alternative ↊ ↋ (U+218A / U+218B).

**Why:** X and E can be typed on any keyboard and work in plain text; ↊ ↋ are the Unicode standard glyphs for
typeset documents. Primel plans the same pair (Pitman's digits) and uses the lookalikes ᘔ Ɛ only until fonts
catch up. Kept after review, even though software reads E as an exponent (a spreadsheet turns
6E62 into 6 × 10^62) and hexadecimal uses E for fourteen. Rejected: lowercase x and e (software reads 6e62
the same way); A and B as in hexadecimal (A = dek, B = el) - safe in software, but they lose the link
to the spoken names dek and el.

**Advantage:** dozenal numbers can be written anywhere - keyboard, plain text, handwriting - and still match the spoken dek and el.

- In data files, write ↊ ↋ or store dozenal numbers as text (quoted), so software can't misread them.
  Quoting also protects the semicolon, which some files use to separate fields

### Seven-segment displays

**Proposed (not decided):** on seven-segment displays (clocks, calculators, meters), dek is shown as
Antonio Ramieri's glyph - the top right, bottom right, bottom left and middle segments, like an upside-down
h - and el as E.

**Why:** a seven-segment display has no diagonals, so X can't be shown, and neither can Pitman's ↊ (on the
display, a 2 turned upside down is still a 2). Ramieri suggested his digits in Facebook's Dozenal (Base 12)
Advocacy group, and they were recorded on rdm.sh in 2009. His dek isn't a letter, so it doesn't clash with
hex or dozenal hex, and no other digit turns into it through one dead segment. El stays E: it matches the
written el, and it's also the shape Pitman's ↋ (a turned 3) takes on the display.

**Advantage:** a dozenal clock or calculator can be built from ordinary display parts, and reads the same
as printed dozenal.

![Dozenal digits on a seven-segment display: 0 to 9 as usual, Ramieri's dek, el as E, and Ramieri's own el (an arch) for comparison.](figures/seven-segment.svg)

- Still to decide: Ramieri's own el is an arch (every segment but the middle and bottom). It avoids hex's E
  (fourteen), but dozenal hex keeps E as eleven anyway, and the arch is a 0 with its bottom segment missing,
  so one dead segment would turn a 0 into an el
- Also considered for dek: H (clashes with nothing, but nobody uses it yet) and A (hex's ten, so existing
  displays already show it, but dozenal hex uses A for twelve)
- Fourteen- and sixteen-segment displays, dot matrices and screens can show X and E as written
