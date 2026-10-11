# The Paludal system

Numbers are dozenal unless marked "(dec)".

**Version 0.3**, 11 Oct 6859 DH (2026 CE). See Versions in Part 4 for what changed.

Paludal is a set of units, like metric, but counted in twelves instead of tens. This page is the short
version: how to count, the handful of units you'd use every day, and how to tell the time. Everything
else - the reasons behind each choice, and the less common units - is in the chapters that follow.

### Counting in twelves

You already count in twelves more than you might think: twelve hours on a clock, twelve months in a year,
twelve eggs in a carton, twelve inches in a foot. Dozenal writes these numbers with digits of their own.

It needs two more digits: **X** (said "dek") for ten and **E** ("el") for eleven. On a clock face, only the
top three numbers change. Twelve, at the top, is written **10** and said "do": one full turn and nothing
over.

![A clock face in dozenal: 1 to 9 stay the same, ten and eleven become X and E, and twelve becomes 10.](figures/clock-face.svg)

| Dozenal | Said | You know it as |
|---|---|---|
| X, E | dek, el | ten, eleven o'clock |
| 10 | do | a dozen: a carton of eggs, a foot of inches, a year of months |
| 16 | do six | a dozen and a half |
| 20 | two do | two dozen: the hours in a day |
| 100 | gro | a gross: a dozen dozen |
| 1,000 | mo | a dozen gross (1,728 dec) |

The semicolon is the dozenal point, said "dit". After it come twelfths, the marks around a clock face:

| Dozenal | Said | You know it as |
|---|---|---|
| 0;1 | zero dit one | a twelfth: one month of a year, five minutes of an hour |
| 0;3 | zero dit three | a quarter: quarter past is the minute hand at 3 |
| 0;4 | zero dit four | a third: four months of a year |
| 0;6 | zero dit six | a half: six inches of a foot, half past |

Twelve splits evenly into halves, thirds, quarters and sixths, so those are all short, exact numbers.

### The everyday units

Each one is close to something you already know.

| Unit | Symbol | Size | About as big as | For example |
|---|---|---|---|---|
| pace | p | 1.45 m | a long stride (two steps) | an adult is about 1;2 p tall |
| dig | di | 1.01 cm | a centimetre | a credit card is 8;6 di long |
| iter | ir | 2.51 km | a mile and a half | a 5 km run is about 2 ir |
| lib | li | 1.77 kg | a big bag of sugar | a newborn baby is about 2 li, an adult 36 li |
| cub | cu | 1.77 L | a big bottle of drink | a wine bottle is 0;5 cu, a bucket 5;6 cu |
| tep | °t | 0.694 °C | a little under a degree Celsius | room 26 °t, body 45 °t |

- A cub of water weighs a lib, as a litre of water weighs a kilogram
- Water freezes at 0 °t and boils at 100 °t

### Bigger and smaller

Like metric's milli-, centi- and kilo-, Paludal has prefixes for smaller and bigger sizes, but each step is
twelve instead of ten:

| Prefix | Symbol | Means | Like | For example |
|---|---|---|---|---|
| tricia- | t↓ | ÷ 1,000 (1,728 dec) | milli- | tcli ≈ 1 gram: an egg is about 50 tcli |
| bicia- | b↓ | ÷ 100 (144 dec) | centi- | the dig is a bicia-pace |
| uncia- | u↓ | ÷ 10 (12 dec) | deci- | the unc is an uncia-pace |
| unqua- | u↑ | × 10 (12 dec) | | uqp ≈ 17.4 m |
| biqua- | b↑ | × 100 (144 dec) | hecto- | bqp ≈ 209 m |
| triqua- | t↑ | × 1,000 (1,728 dec) | kilo- | the iter is a triqua-pace |

- The most-used sizes have short names of their own - dig, unc, iter - and those are used instead
- The arrow shows the direction: ↓ divides, ↑ multiplies. Typed without arrows, ↓ is c and ↑ is q (`tcli`)
- Length and Time (Part 2) have tables for converting between all the named units

### Telling the time

The day is cut into twelves, and each cut is one digit of the time.

| Unit | Symbol | Size | How many |
|---|---|---|---|
| chime | ch | 2 hours | 10 (12 dec) in a day |
| spell | sl | 10 minutes | 10 (12 dec) in a chime |
| moment | mt | 50 seconds | 10 (12 dec) in a spell |
| breath | br | 4.17 seconds | 10 (12 dec) in a moment |
| *beat* | bt | 1.04 seconds - about a second | 4 in a breath |

Units in *italics* aren't a power of twelve: a beat is 3 blinks, not a twelfth or a dozen of anything.

The time is written as three digits, counting moments since midnight:

| Time | Paludal | Now |
|---|---|---|
| Midnight | 000 | 00:00 |
| Dawn | 300 | 06:00 |
| Noon | 600 | 12:00 |
| Dusk | 900 | 18:00 |
| Late evening | E91 | 23:31 |

Half an hour is 3 spells, an hour is 6 spells (half a chime), and a film is about one chime.

### How it fits together

![How Paludal is built: the day gives the blink, light gives the pace, and a cube of water gives the lib - counted in twelves at every step.](figures/idea.svg)

Like SI, every unit is fixed to a constant of nature, so each one converts exactly to metric. The
chapters below explain how: Principles covers the ideas behind the system, and Names lists every unit.
To get a feel for the sizes, start with Thinking in Paludal in Part 3 (Everyday use).
