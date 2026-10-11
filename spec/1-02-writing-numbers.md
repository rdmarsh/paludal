## Writing numbers

**Decided:** decimal uses a dot (eg 3.14); dozenal uses a semicolon (3;18481).

**Why:** the punctuation shows which base a number is in, so the two can't be confused.

**Advantage:** the base of any number can be seen at a glance, even with no unit or marker.

**Decided:** long numbers are grouped in threes with commas, in both bases: 100,000 (dozenal), 86,400 (dec).
Four-digit numbers are grouped too (1,728). Not grouped: years (2026 CE, 6859 DH), dates, times of day
(EX0;53), and digits after the point.

**Why:** groups of three are the easiest for people to read, and they match how numbers are spoken
(thousand / million, mo / bimo). The comma is free in both bases, since decimal uses a dot as the point and
dozenal a semicolon. It replaces SI's thin space (86 400), which is easy to miss, gets lost when text is
copied, and can split a number across two lines. Where the comma is the decimal point (much of Europe),
86,400 could be misread; the dot-and-semicolon rule above already settles which mark is the point.

**Advantage:** long numbers are easy to read, copy and say, in either base.

- eg 0;4 is 4/10; (a third), or 0.333... (dec)

**Decided:** documents number their pages, parts, chapters, sections, tables and figures in dozenal, with X
and E (page 2X, chapter 1E, section 1E.3, figure 15.1). The dot between levels is a separator, not a point,
as in version numbers. The PDF of this spec does this.

**Why:** asked for (2026 CE): every number in the system is dozenal, and a document about it shouldn't count
its own pages in decimal. X and E rather than ↊ ↋, so page numbers match the spec's text.

**Advantage:** a reader practises dozenal just by finding a page, and nothing in the document mixes bases.

Halves, thirds, quarters and sixths all end after one digit. The catch: a quarter is 0;3 and a third is
0;4, the opposite of what the digits suggest. Fifths and tenths recur, as thirds do in decimal.

| Fraction        | Dozenal      | Decimal   |
|-----------------|--------------|-----------|
| 1/2             | 0;6          | 0.5       |
| 1/3             | 0;4          | 0.333...  |
| 2/3             | 0;8          | 0.666...  |
| 1/4             | 0;3          | 0.25      |
| 3/4             | 0;9          | 0.75      |
| 1/6             | 0;2          | 0.1666... |
| 1/8             | 0;16         | 0.125     |
| 3/8             | 0;46         | 0.375     |
| 1/9             | 0;14         | 0.111...  |
| 1/12 (dec)      | 0;1          | 0.0833... |
| 1/16 (dec)      | 0;09         | 0.0625    |
| 1/5             | 0;2497 2497... | 0.2     |
| 1/10 (dec)      | 0;1 2497 2497... | 0.1   |
| 1/7             | 0;186X35 186X35... | 0.142857... |

**Decided:** the dozenal percent is **per gro** (per 144 dec), written **/gro**: 75% = 0;9 = 90 /gro; 65% ≈ 0;7X = 7X /gro.

**Why:** it parallels "per cent" (Latin centum is the number word, as gro is ours). The two digits after
the semicolon are already the per-gro figure, so nothing needs converting. "Per bicia" was rejected: bicia
already means ÷100;, so "per bicia" would mean ×100;. % can't be reused - it would be read as decimal. No
established dozenal symbol is known, so /gro is used for now.

**Advantage:** a per-gro figure is read straight off a fraction, with no arithmetic.

**Decided:** fractions (numbers below one) always have a leading zero: 0;6, never ;6.

**Why:** a bare leading semicolon is easy to miss or mistake for punctuation, and it keeps a semicolon
at the start of a number from ever being ambiguous.

**Advantage:** a fraction can never lose its point in print or handwriting.

**Decided:** how to tell dozenal and decimal numbers apart, when both are in use:

1. A number with a unit needs no marker: the unit says which system (46 p is dozenal, 54 m is decimal).
2. A number containing X or E is dozenal.
3. Each document states its default base (this one: dozenal).
4. A bare number in mixed text is marked: dozenal with a trailing semicolon (**46;**), decimal with
   **(dec)**, or a subscript ᵈ in typeset documents. Small numbers that read the same in both (0-9)
   and number words (twelve) need no marker.
5. Years: CE years are decimal (2026 CE), DH years are dozenal (6859 DH).
6. Colour can be added on screen, but never as the only signal.

**Why:** most real numbers carry a unit, so they're already unambiguous; markers are only needed for bare
numbers. The trailing semicolon is just the dozenal point with nothing after it (like "46." in decimal),
so it works in plain text and handwriting without any new symbol. Colour fails in print, handwriting,
plain text and for colour-blind readers. Numeric subscripts (46₁₂) were rejected: "12" is itself
ambiguous - in dozenal it means fourteen. Years get their era instead of a marker because
the era is already written with years (CE / DH), so it costs nothing extra.

**Advantage:** mixed text stays unambiguous with almost no extra marks, in any medium and for any reader.
