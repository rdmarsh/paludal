# Build the Paludal docs from the spec (spec/*.md, one file per chapter) with pandoc. Needs GNU make 4.4 or later
# (on macOS: brew install make, then run gmake).
#
#   make            docs/, the website: one page per chapter (committed; GitHub Pages serves it)
#   make all        docs/ plus out/paludal.{xml,tex,pdf,adoc}
#   make docbook | latex | pdf | asciidoc
#   make clean      remove out/
#
# Needs pandoc 3.8+ (brew install pandoc, or make PANDOC=/path/to/pandoc). The PDF also needs
# XeLaTeX and memoir (brew install --cask basictex; sudo tlmgr install memoir newunicodechar etoolbox fvextra)
# and the fonts DejaVu Sans, Noto Sans Symbols (for ↊ ↋) and Noto Sans Canadian Aboriginal (for ᘔ). Diagrams in the PDF need
# mermaid-cli (npm install -g @mermaid-js/mermaid-cli, or make MMDC=/path/to/mmdc); without it
# the PDF says to see paludal.org instead. The SVG figures (figures/) need rsvg-convert
# (brew install librsvg, or make RSVG=/path/to/rsvg-convert), with the same fallback.

ifeq ($(filter-out 3.% 4.0% 4.1% 4.2% 4.3%,$(MAKE_VERSION)),)
$(error GNU make 4.4 or later is needed, this is $(MAKE_VERSION))
endif

MAKEFLAGS += --no-builtin-rules --warn-undefined-variables
.SUFFIXES:
.DELETE_ON_ERROR:

PANDOC  ?= pandoc
XELATEX ?= xelatex
MMDC    ?= mmdc
RSVG    ?= rsvg-convert

# Files are read in name order: N-MM-name.md is chapter MM of part N (00 is the part's opening)
SRC    := $(sort $(wildcard spec/*.md))
SITE   := docs
FILTER := pandoc/paludal.lua
DEPS   := $(SRC) $(FILTER) Makefile
OUT    := out

# Every format reads the same source through the same filter
pandoc = $(PANDOC) -f gfm$(smart) -s --lua-filter $(FILTER) $(SRC)
smart :=
# The version comes from the "**Version x.y**" line at the top of the spec
VERSION := $(shell sed -n 's/^\*\*Version \([^*]*\)\*\*.*/\1/p' spec/0-00-index.md)
titled = -M title=Paludal -M subtitle="A dozenal system of units" -M date="Version $(VERSION)"

# mermaid-cli draws each diagram in the spec as out/diagrams/paludal-N.pdf, numbered in order
diagrams := $(if $(shell command -v $(MMDC)),$(OUT)/diagrams/paludal.md)
# rsvg-convert draws each figures/NAME.svg as out/figures/NAME.pdf
figures := $(wildcard figures/*.svg)
figure_pdfs := $(if $(shell command -v $(RSVG)),$(figures:%.svg=$(OUT)/%.pdf))

.DEFAULT_GOAL := html
.PHONY: html all docbook latex pdf asciidoc clean

html:     $(SITE)/index.html
docbook:  $(OUT)/paludal.xml
latex:    $(OUT)/paludal.tex
pdf:      $(OUT)/paludal.pdf
asciidoc: $(OUT)/paludal.adoc
all: html docbook latex pdf asciidoc

# Pandoc writes index.html and the filter writes the other pages beside it; old pages go first
# so a renamed chapter leaves nothing behind
$(SITE)/index.html: $(DEPS) pandoc/template.html $(figures)
	rm -f $(SITE)/*.html
	$(pandoc) -t html5 --template pandoc/template.html --syntax-highlighting=none --wrap=none -o $@

$(OUT)/paludal.xml: $(DEPS) | $(OUT)
	$(pandoc) $(titled) -t docbook5 -o $@

$(OUT)/paludal.adoc: $(DEPS) | $(OUT)
	$(pandoc) $(titled) -t asciidoc -o $@

# Print gets curly quotes and apostrophes
$(OUT)/paludal.tex: smart := +smart
$(OUT)/paludal.tex: $(DEPS) pandoc/header.tex $(diagrams) $(figure_pdfs) | $(OUT)
	$(pandoc) $(titled) -M author="David Marsh" -t latex -o $@ -M diagrams=$(OUT)/diagrams/paludal- \
	  -V documentclass=memoir -V classoption=oneside,openany,titlepage -V papersize=a4 -V fontsize=10pt \
	  -V geometry:margin=2cm -V mainfont="DejaVu Sans" -V monofont="DejaVu Sans Mono" -V colorlinks=true \
	  --top-level-division=part --toc --toc-depth=1 -H pandoc/header.tex

# Three runs settle the table of contents and longtable widths. XeLaTeX exits non-zero on
# warnings, so success is judged by the PDF appearing.
$(OUT)/paludal.pdf: $(OUT)/paludal.tex
	rm -f $@
	for i in 1 2 3; do $(XELATEX) -interaction=nonstopmode -output-directory=$(OUT) $< >/dev/null || true; done
	test -s $@
	@echo "overfull boxes: $$(grep -c Overfull $(OUT)/paludal.log || true)"
	@echo "missing glyphs: $$(grep -c 'Missing character' $(OUT)/paludal.log || true)"

$(OUT)/paludal.md: $(SRC) | $(OUT)
	cat $(SRC) > $@

$(OUT)/diagrams/paludal.md: $(OUT)/paludal.md pandoc/mermaid.json | $(OUT)/diagrams
	$(MMDC) -q -i $< -o $@ -e pdf -c pandoc/mermaid.json

$(OUT)/figures/%.pdf: figures/%.svg | $(OUT)/figures
	$(RSVG) -f pdf -o $@ $<

$(OUT) $(OUT)/diagrams $(OUT)/figures:
	mkdir -p $@

clean:
	rm -rf $(OUT)
