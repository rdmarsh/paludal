# Build the Paludal docs from ideas.md with pandoc. Needs GNU make 4.4 or later
# (on macOS: brew install make, then run gmake).
#
#   make            index.html, the quick-view page (committed)
#   make all        index.html plus out/paludal.{xml,tex,pdf,adoc}
#   make docbook | latex | pdf | asciidoc
#   make clean      remove out/
#
# Needs pandoc 3.8+ (brew install pandoc, or make PANDOC=/path/to/pandoc). The PDF also needs
# XeLaTeX and memoir (brew install --cask basictex; sudo tlmgr install memoir newunicodechar etoolbox fvextra)
# and the fonts DejaVu Sans and Noto Sans Symbols (for ↊ ↋). Diagrams in the PDF need
# mermaid-cli (npm install -g @mermaid-js/mermaid-cli, or make MMDC=/path/to/mmdc); without it
# the PDF says to see index.html instead. The SVG figures (figures/) need rsvg-convert
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

SRC    := ideas.md
FILTER := pandoc/paludal.lua
DEPS   := $(SRC) $(FILTER) Makefile
OUT    := out

# Every format reads the same source through the same filter
pandoc = $(PANDOC) -f gfm$(smart) -s --lua-filter $(FILTER) $(SRC)
smart :=
# The version comes from the "**Version x.y**" line at the top of the spec
VERSION := $(shell sed -n 's/^\*\*Version \([^*]*\)\*\*.*/\1/p' $(SRC))
titled = -M title=Paludal -M subtitle="A dozenal system of units" -M date="Version $(VERSION)"

# mermaid-cli draws each diagram in the source as out/diagrams/ideas-N.pdf, numbered in order
diagrams := $(if $(shell command -v $(MMDC)),$(OUT)/diagrams/ideas.md)
# rsvg-convert draws each figures/NAME.svg as out/figures/NAME.pdf
figures := $(wildcard figures/*.svg)
figure_pdfs := $(if $(shell command -v $(RSVG)),$(figures:%.svg=$(OUT)/%.pdf))

.DEFAULT_GOAL := html
.PHONY: html all docbook latex pdf asciidoc clean

html:     index.html
docbook:  $(OUT)/paludal.xml
latex:    $(OUT)/paludal.tex
pdf:      $(OUT)/paludal.pdf
asciidoc: $(OUT)/paludal.adoc
all: html docbook latex pdf asciidoc

index.html: $(DEPS) pandoc/template.html $(figures)
	$(pandoc) -t html5 --template pandoc/template.html --syntax-highlighting=none --wrap=none -o $@

$(OUT)/paludal.xml: $(DEPS) | $(OUT)
	$(pandoc) $(titled) -t docbook5 -o $@

$(OUT)/paludal.adoc: $(DEPS) | $(OUT)
	$(pandoc) $(titled) -t asciidoc -o $@

# Print gets curly quotes and apostrophes
$(OUT)/paludal.tex: smart := +smart
$(OUT)/paludal.tex: $(DEPS) pandoc/header.tex $(diagrams) $(figure_pdfs) | $(OUT)
	$(pandoc) $(titled) -M author="David Marsh" -t latex -o $@ -M diagrams=$(OUT)/diagrams/ideas- \
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

$(OUT)/diagrams/ideas.md: $(SRC) pandoc/mermaid.json | $(OUT)/diagrams
	$(MMDC) -q -i $< -o $@ -e pdf -c pandoc/mermaid.json

$(OUT)/figures/%.pdf: figures/%.svg | $(OUT)/figures
	$(RSVG) -f pdf -o $@ $<

$(OUT) $(OUT)/diagrams $(OUT)/figures:
	mkdir -p $@

clean:
	rm -rf $(OUT)
