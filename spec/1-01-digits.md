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
