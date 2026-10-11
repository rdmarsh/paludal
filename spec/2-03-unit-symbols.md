## Unit symbols

**Decided:** first two letters of the name, lowercase. Exceptions: pace = **p** (most used, and "pa" would
clash with Pa), vig = **vg** (vi is vis), grex = **gx** (gr = grain). No symbol may clash with an SI or
imperial symbol, since both systems will be in use side by side.

**Why:** one simple rule is easy to learn and guess. Symbols must not clash with SI or imperial ones because both systems will be in use side by side for a long time. Pace gets a single letter because it's used most.

**Advantage:** a symbol can be guessed from its name (and the name from the symbol), and never means something else in SI or imperial.

**Decided:** where the first two letters make a common English word, use the first and last letters instead,
as the moment does (mt): beat = **bt** (not be), iter = **ir** (not it), onus = **os** (not on).

**Why:** a review found that "add 3 it", "2 on of charge" and "1;3 be" read as English. opus keeps **op**:
its first and last letters (os) would be the onus, and "op" isn't a common word on its own.

**Advantage:** no symbol reads as an English word, so a quantity can't be mistaken for text.

| Unit   | Symbol | Quantity |
|--------|--------|----------|
| blink  | bl     | time |
| beat   | bt     | time |
| breath | br     | time |
| moment | mt     | time |
| chime  | ch     | time |
| pace   | p      | length |
| unc    | un     | length |
| dig    | di     | length |
| span   | sp     | length |
| ulna   | ul     | length |
| gress  | gs     | length |
| iter   | ir     | length |
| navis  | na     | length (sea and air) |
| parax  | px     | length (stars) |
| lib    | li     | mass |
| cub    | cu     | volume |
| ager   | ag     | area |
| tep    | °t     | temperature |
| tep absolute | ta | absolute temperature |
| vis    | vi     | force |
| opus   | op     | energy |
| vig    | vg     | power |
| pres   | pr     | pressure |
| riv    | ri     | current |
| onus   | os     | charge |
| imp    | im     | voltage |
| grex   | gx     | amount |
| lam    | la     | light |
| vox    | vo     | sound level |
| turn   | tu     | angle |

- chime: **ch** (the imperial chain is no longer used, so no real clash)
- moment: **mt** (first and last letters: "mo" is the spoken word for 1,000, and mm is the millimetre)

**Decided:** temperature uses **°t** (eg 25 °t), for readings and differences alike, like °C. It's written
with a space between the number and the degree sign, as SI writes 25 °C: 25 °t (and 25 °C, 77 °F when those
appear). In typeset text the space is non-breaking, so a temperature can't be split across a line.
Plain-ASCII fallback: **te**. A bare "25°" is fine where tep is the expected scale (eg weather).

**Why:** the degree sign means "a scale with a chosen zero", which is what the tep is (0 = freezing, like
Celsius), and people already read 25 °C / °F that way. Lowercase because tep isn't named after a person
(°C and °F are), and it avoids T (tesla). It's still two characters, so it fits the spirit of the rule.
Written with a space like every other unit symbol (5;6 li, 29 im), and as SI and ISO 80000 write °C: the
only SI symbols written straight after the number are the degree, minute and second of angle. Replaces the
earlier rule of no space (25°t), which broke that consistency; a non-breaking space keeps the number and
its unit on one line.

**Advantage:** readings look like the °C and °F people already know, can't be confused with the tesla, and
temperatures follow the same spacing rule as every other unit.

- Examples: 1;3 p tall, 2;6 li, 25 °t, 68 p/br, 29 im

**Decided:** all unit and prefix symbols are lowercase (tqop, not tqOP or TQop).

**Why:** every prefix ends in q or c, so the boundary between prefix and unit is already clear. Capitals
would clash with chemical elements (Cu, Be, Br, La), and all-capital units read as acronyms. Reusing SI
prefix letters for powers of twelve (k = ×1,000;) was rejected: the same letter meaning a 1.728× different
factor would cause errors where both systems are in use.

**Advantage:** there's nothing to remember about case, and no symbol can be mistaken for a chemical element or an SI prefix.

**Decided:** no unit symbol may start with **q**.

**Why:** in a prefix symbol, q is both quad's letter (4) and the "multiply" ending. If a unit symbol started
with q, a prefixed symbol could be read two ways: "uqq..." could be uq (×10) followed by the unit, or uqq
(×10^14) followed by the rest. c is safe, because no digit root uses it, so cu and ch are fine.

**Advantage:** every prefixed symbol can be read only one way, without checking a list of units.
