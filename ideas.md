# The Paludal system

Ideas for a dozenal based system similar to metric or to replace SI units with.

**Decided:** the system is called **Paludal** ("paludal units", "is that metric or paludal?").
Fallbacks if needed: **Uncial** (Latin uncia, a twelfth) or **Passic** (from passus, the pace - as metric is from the metre).

**Why:** named after its creator, as Fahrenheit, Celsius and Kelvin are - but hidden: Latin *palus, paludis*
means "a marsh". It matches the Latin naming style of the units, and works as an adjective like "metric".

Numbers below are dozenal unless marked "(dec)".

Goals: as rigorous as SI (every unit defined by a fixed constant, exact conversion to SI),
but human focused - everyday sizes and rules of thumb matter more than round constants.

# Summary

## Base units and defining constants

| Quantity    | Unit  | Size (SI)              | Defined by (exact)                            | Named after |
|-------------|-------|------------------------|-----------------------------------------------|---|
| Time        | blink | 0.347222 s (25/72 s)   | 1 breath (10 blinks) = 750E583273 caesium periods | English: the blink of an eye |
| Length      | pace  | 1.452545 m             | c = 2 × 10^7 paces/blink                      | Latin passus, a pace |
| Mass        | lib   | 1.771431 kg            | h = 2;13 × 10^-28                             | Latin libra, pound / scales |
| Temperature | tep   | 0.694346 K             | k = 2;07 × 10^-1E, 0 tep = 273.15 K (freezing) | Latin tepor, warmth |
| Current     | riv   | 1.0237 A               | e = 1 × 10^-15 onus                           | Latin rivus, stream |
| Amount      | grex  | 6.17235 × 10^23 (dec) things | 1 grex = 1;15 × 10^1X things            | Latin grex, flock |
| Light       | lam   | 1 cd                   | same as SI candela (K_cd = 683 lm/W dec)      | Latin lampas, lamp |

## Derived and everyday units

| Quantity          | Unit | Size (SI)        | Named after |
|-------------------|------|------------------|---|
| Beat              | beat | 1.04167 s (3 blinks, 25/24 s) | English: a heartbeat |
| Clock unit        | breath | 4.16667 s (10 blinks = 4 beats) | English: one breath |
| Dozenal hour      | chime | 2 hours exactly (1000 breaths, 0;1 day) | English: clocks chime on the hour |
| Dozenal minute    | moment | 50 s exactly (0;01 chime, 10 breaths) | English moment, from Latin momentum |
| 1/10 pace         | unc  | 12.1 cm          | Latin uncia, a twelfth |
| 1/100 pace        | dig  | 1.01 cm          | Latin digitus, finger |
| Volume (unc³)     | cub  | 1.7736 L         | Latin cubus, cube |
| Force             | vis  | ≈ 21.3 N         | Latin vis, force |
| Energy            | opus | ≈ 31.0 J         | Latin opus, work |
| Power             | vig  | ≈ 89.3 W         | Latin vigor, liveliness |
| Pressure          | pres | ≈ 10.1 Pa        | Latin pressus, pressed |
| Charge            | onus | ≈ 0.3555 C       | Latin onus, load |
| Voltage           | imp  | ≈ 87.21 V        | Latin impetus, push |

## Rules of thumb

- A cub of water weighs a lib (0.9994 at 20 °C). A dig-cube of water ≈ 1/1000 lib ≈ 1 g.
- Time of day = chime;moments (d;dd), like hours:minutes: 0;00 midnight, 3;00 dawn, 6;00 noon, 9;00 dusk.
- A moment (50 s) is about a minute; a beat (1.04 s) is about a second.
- 100 km/h ≈ 68 paces/breath; motorway limit 70 (105 km/h).
- Water freezes at 0 tep, boils at ≈ 100 tep. Body ≈ 45;3 tep.
- 240 V mains ≈ 2;9 imp, 120 V ≈ 1;46 imp.
- A 6 ft person ≈ 1¼ paces. 1 inch ≈ 2;6 digs.

# Symbols

**Decided:** digits 0 1 2 3 4 5 6 7 8 9 X E (X = ten, E = eleven); print alternative ↊ ↋ (U+218A / U+218B).

**Why:** X and E can be typed on any keyboard and work in plain text; ↊ ↋ are the Unicode standard glyphs for
typeset documents.

## Unit symbols

**Decided:** first two letters of the name, lowercase. Exceptions: pace = **p** (most used, and "pa" would
clash with Pa), vig = **vg** (vi is vis), grex = **gx** (gr = grain). No symbol may clash with an SI or
imperial symbol, since both systems will be in use side by side.

**Why:** one simple rule is easy to learn and guess. Symbols must not clash with SI or imperial ones because both systems will be in use side by side for a long time. Pace gets a single letter because it's used most.

| Unit  | Symbol | | Unit  | Symbol | | Unit  | Symbol |
|-------|--------|-|-------|--------|-|-------|--------|
| blink | bl     | | lib   | li     | | pres  | pr     |
| beat  | be     | | cub   | cu     | | riv   | ri     |
| breath | br    | |       |        | |       |        |
| pace  | p      | | tep   | °t     | | onus  | on     |
| unc   | un     | | vis   | vi     | | imp   | im     |
| dig   | di     | | opus  | op     | | grex  | gx     |
|       |        | | vig   | vg     | | lam   | la     |
|       |        | |       |        | | vox   | vo     |

- chime: **ch** (the imperial chain is no longer used, so no real clash)
- moment: **mt** (first and last letters: "mo" is the spoken word for 1000, and mm is the millimetre)

**Decided:** temperature uses **°t** (eg 25 °t), for readings and differences alike, like °C. Plain-ASCII
fallback: **te**. A bare "25°" is fine where tep is the expected scale (eg weather).

**Why:** the degree sign means "a scale with a chosen zero", which is what the tep is (0 = freezing, like
Celsius), and people already read 25 °C / °F that way. Lowercase because tep isn't named after a person
(°C and °F are), and it avoids T (tesla). It's still two characters, so it fits the spirit of the rule.
- Examples: 1;3 p tall, 2;6 li, 25 °t, 68 p/br, 2;9 im

## Prefix symbols

**Decided:** initials of the SDN digit roots, then **q** (multiply) or **c** (divide). The last letter is always
q or c, so a symbol can always be read unambiguously.

**Why:** built from the SDN roots we already use, so there's no separate table to memorise. Ending in q or c keeps them unambiguous even though some roots share initials (quad / qua).

| Digit  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | X | E |
|--------|---|---|---|---|---|---|---|---|---|---|---|---|
| Root   | nil | un | bi | tri | quad | pent | hex | sept | oct | enn | dek | el |
| Letter | n | u | b | t | q | p | h | s | o | e | d | l |

- uq ×10, bq ×100, tq ×1000, unq ×10^10; uc ÷10, bc ÷100, tc ÷1000
- Prefix goes straight onto the unit symbol: 3 tqp = 3 triqua-paces, 5 bcli = 5 bicia-libs
- The named sizes keep their own symbols: unc = un (= ucp), dig = di (= bcp)
- el's letter is **l** ("el" is how L is said); e is taken by enn
- Watch: enn's "e" (9) is easily confused with the digit E (el); bq looks like Bq (becquerel)

## Spoken numbers

**Decided:** digits X = **dek**, E = **el** (the DSA standard names). Powers use **do / gro / mo**:

**Why:** dek and el are the established standard names, so we use them (and changed the prefix roots to match, not the other way round). Calling 10; "ten" would be heard as decimal. do / gro / mo are short, and bimo / trimo extend them the way million / billion extend thousand.

| Number | Name  | (dec)    |
|--------|-------|----------|
| 10     | do    | 12       |
| 100    | gro   | 144      |
| 1000   | mo    | 1728     |
| 10^6   | bimo  | 2985984  |
| 10^9   | trimo | 5.16 × 10^9 |

- Digits are grouped in threes, like thousand / million: 4,000,000 = four bimo
- 46 = "four do six", 2X3 = "two gro dek do three", 6E62 = "six mo el gro six do two"
- Never say "ten" for 10; - it gets heard as decimal
- Codes, phone numbers etc. are read digit by digit; after the semicolon, always digit by digit
  (3;14 = "three point one four")

# Writing numbers

**Decided:** decimal uses a dot (eg 3.14); dozenal uses a semicolon (3;18481).

**Why:** the punctuation shows which base a number is in, so the two can't be confused.

- eg 0;4 is 4/10; (a third), or 0.333... (dec)

**Decided:** fractions (numbers below one) always have a leading zero: 0;6, never ;6.

**Why:** a bare leading semicolon is easy to miss or mistake for punctuation, and it keeps a semicolon
at the start of a number from ever being ambiguous.

**Decided:** how to tell dozenal and decimal numbers apart, when both are in use:

1. A number with a unit needs no marker: the unit says which system (46 p is dozenal, 54 m is decimal).
2. A number containing X or E is dozenal.
3. Each document states its default base (this one: dozenal).
4. A bare number in mixed text is marked: dozenal with a trailing semicolon (**46;**), decimal with
   **(dec)**, or a subscript ᵈ in typeset documents. Small numbers that read the same in both (0-9)
   and number words (twelve) need no marker.
5. Years: CE years are decimal (2026 CE), HE years are dozenal (6E62 HE).
6. Colour can be added on screen, but never as the only signal.

**Why:** most real numbers carry a unit, so they're already unambiguous; markers are only needed for bare
numbers. The trailing semicolon is just the dozenal point with nothing after it (like "46." in decimal),
so it works in plain text and handwriting without any new symbol. Colour fails in print, handwriting,
plain text and for colour-blind readers. Numeric subscripts (46₁₂) were rejected: "12" is itself
ambiguous - in dozenal it means fourteen. Years get their era instead of a marker because
the era is already written with years (CE / HE), so it costs nothing extra.

# Time

**Decided:** base unit **the blink** = 1/10 breath ≈ 0.34722 seconds (1/100000 of a day)

**Decided:** **beat** = 3 blinks = 0;3 breath = 25/24 s ≈ 1.04 s - the nearest thing to a second.
Clock unit: the **breath** = 10 blinks = 4 beats = 1/10000 of a day (1/20736 dec) ≈ 4.16667 seconds.

**Why:** the time units are named after the body's own rhythms - a blink of the eye, a heartbeat, a breath -
which suits a human-focused system and makes a memorable set (blink, beat, breath). The sizes fit: a blink
lasts ~0.1-0.4 s, a resting heart beats ~once a second, and a resting breath (or one "in for 4" count in
meditation) is ~4 s. The beat was added because people need a second-sized unit (counting, timing, music).
Rejected: tick for 0.35 s (a clock tick is ~1 s); tick / tock (clock words don't pair with breath); pulse.
The old 4.17 s "tick" is now the breath. Clocks can still "tick" each beat informally. Removed: the wink (half a blink, 0.17 s) - too fast to be
useful at human scale.

**Why:** with the breath as base, derived units are tiny (force 0.148 N, power 0.052 W).
With the blink: force ≈ 21.3 N, energy ≈ 31 J, power ≈ 89 W, pressure ≈ 10.1 Pa - human-sized.

- Blink is the base for physics; beat and breath are the everyday units (like the second and minute in SI).
- Human scale: reaction time ≈ 3/4 blink, heartbeat 2-3 blinks, 100 m sprint ≈ 28 (dec) blinks

- days divided into 10000 breaths (twelve to the 4th power = 20736 dec)
  - 0;1    day = 2 hours (1 chime)
  - 0;01   day = 10 minutes
  - 0;001  day = 50 seconds (1 moment)
  - 0;0001 day = 1 breath ≈ 4.1667 seconds

**Decided:** the **chime** = 0;1 day = 1000 breaths = 2 hours exactly, the dozenal hour (clocks chime on the
hour). Rejected: bell (sounds like the bel, B; ship's bells are half-hours), hora, mark.

**Why:** people use hours constantly, so the dozenal system needs an hour-sized unit; 0;1 day is the 2-hour mark on the twelve-mark dial. "Chime" is what clocks do on the hour.

**Decided:** the **moment** (symbol **mt**) = 0;01 chime = 10 breaths = 50 s exactly - the dozenal minute.

**Why:** time of day works like hours, minutes and seconds: three named parts. The chime is the hour, the
moment the minute (two digits, read by the long hand against fine marks), the breath the second. The
10-minute digit (0;1 chime) needs no name, just as "ten minutes" doesn't. "Wait a moment" already means about
a minute, and the medieval moment was a unit of time (90 s).

**Decided:** time of day is written **d;dd** (chime; moments) or **d;ddd** with breaths - like 21:45 and 21:45:30.

**Why:** people handle 3-digit groups more easily than 4, the first digit matches the clock dial, and the
groups match the clock's three hands.

| Time   | Chime | Moments | Breath | Reads                          |
|--------|-------|---------|--------|--------------------------------|
| E;917  | E     | 91      | 7      | el chimes, 91 moments, 7 breaths |
| 6;00   | 6     | 00      |        | noon                           |

- 0;00 = midnight, 6;00 = noon
- the number is in chimes: the time 9;3X0 is the fraction 0;93X day
- durations use the same form: +1;30

**Decided:** times more precise than a breath just add digits, with no separator: E;X053 (3 blinks past
E;X05). On screens, the extra digits are shown smaller or dimmer, like the hundredths on a stopwatch.

**Why:** a time of day is a single number - chimes since midnight - so times can be subtracted and compared
directly (E;X05 - 9;300 = 2;705 chimes ≈ 5 h 10 min). A second semicolon (E;X05;3) would break that, and a space
(E;X05 3) makes the digits look unrelated. Decimal times do the same: 9.58 s, 1:23.45 on a stopwatch.
- spoken like "nine forty-five": E;91 = "el, nine-one"; 6;00 = "six"; with breaths, "el, nine-one, seven"

## Years

**Decided:** year numbering follows the **Human (Holocene) Era**: 1 HE = 10,000 BCE, so add 10,000 (dec) to the CE year.

**Why:** TODO - reason not recorded.

- 2026 CE = 12026 HE (dec) = **6E62 HE**
- Spoken as two pairs, like "twenty twenty-six" (that's how years are said now): 6E62 = "six do el, six do two"
  - round years: 7000 = "seven mo", 6E00 = "six do el gro"

## Calendar

**Decided:** keep the standard Gregorian months and 7-day weeks. Only the numbering changes:
**week numbers** (ISO weeks) are written in dozenal: week 1 to 44 (52 dec), 45 in long years (53 dec).

**Why:** 365 (dec) days can't be split into dozenal-round months, and changing the 7-day week is too big a change. Writing the numbers in dozenal keeps the whole system consistent.

- eg 3 Oct 2026 CE is week 34 (ISO week 40 dec)

**Month names (decided):** the SDN digit roots, used as the names themselves.

**Why:** no new words to learn - each name is the month's number, its prefix root and its spoken digit. It also fixes the Roman misnumbering (September-December were the seventh to tenth months when the year began in March).

| # | Month | Was | | # | Month | Was |
|---|-------|-----|-|---|-------|-----|
| 1 | Un    | Jan | | 7 | Sept  | Jul |
| 2 | Bi    | Feb | | 8 | Oct   | Aug |
| 3 | Tri   | Mar | | 9 | Enn   | Sep |
| 4 | Quad  | Apr | | X | Dek   | Oct |
| 5 | Pent  | May | | E | El    | Nov |
| 6 | Hex   | Jun | | 10 | Do   | Dec |

- Same lengths and dates as the Gregorian months; only the names change
- Fixes the Roman shift: Sept/Oct/Dek are finally the 7th/8th/Xth months (Sept-Dec were named when the year began in March)
- Do = "the dozenth month"
- Rejected: a -men suffix (Latin mensis) - reads as English "men" (Hexmen, Septmen)

**Day of month (decided):** written in dozenal, 1 to 27 (31 dec).

**Why:** every number in the system is dozenal; a date shouldn't mix bases.

- eg today (3 Oct 2026 CE) = 3 Dek 6E62; 31 (dec) Oct = 27 Dek; Christmas = 21 Do

**Possibility (not decided):** the Dozenal Solstice / Holocene calendar (clocks.dozenal.ca):
twelve months of 30 (dec) days, with the 5-6 leftover "S-days" outside any month; often paired with a 6-day week
(divides into halves and thirds). https://clocks.dozenal.ca/pdf/dozenal-calendar.pdf
- A 6-day week would mean a 4-day working week with the usual 2-day weekend
- For now, the 7-day week stays: changing it is too big a change, and 365 (dec) days can't be split evenly anyway

## Analogue clocks

**Decided:** a 24-hour dial with twelve marks, noon at the top, turning clockwise.

**Why:** one turn per day shows the whole day at a glance; noon at the top matches the sun at its highest,
and clockwise keeps the convention people already know.

Three hands, like hour / minute / second:

| Hand    | Turns once per | Reads         | Dial                                   | Like        |
|---------|----------------|---------------|----------------------------------------|-------------|
| Chime   | day            | chime (0-E)   | 12 marks                               | hour hand   |
| Moment  | chime (2 h)    | moments 00-EE | 12 marks + 144 (dec) fine marks        | minute hand |
| Breath  | moment (50 s)  | breath (0-E)  | 12 marks; steps once per beat (4 per mark) | second hand |

- The breath hand moves at about the pace of a second hand, stepping once per beat - clocks still "tick"
- **Noon (6;00) points straight up, midnight (0;00) straight down**
  - dawn ≈ 3;00 on the left, dusk ≈ 9;00 on the right (at the equinoxes)
  - **Clockwise everywhere** (bottom → left → top → right), both hemispheres - matches convention,
    and clocks are clockwise because they copied northern sundials
  - matches the sun's path when facing south in the northern hemisphere, so a correctly
    oriented clock roughly agrees with a sundial
- Existing dozenal clock designs to compare: https://clocks.dozenal.ca (not yet reviewed - blocked by sandbox network policy)

## Caesium definition

**Decided:** 1 breath = 750E583273 caesium periods exactly (38,302,632,375 dec).

**Why:** it makes the breath exactly 25/6 SI seconds, so conversion to SI is exact and the system inherits SI's precision and any future redefinition of the second (details below).

- So 1 blink = 750E58327;3 periods (terminates in dozenal; 3,191,886,031.25 dec)
- Equivalent to: 1 breath = 25/6 SI seconds exactly, so the day stays at exactly 86400 SI seconds.
- Converting between SI and dozenal time is exact (no drift, no leap breaths beyond what SI already needs).
- Leap breaths (like leap seconds) needed only when Earth drifts ~half a breath (~2 s) - roughly 1/4 as often as leap seconds were.
- Survives the planned SI redefinition of the second (optical clocks, ~2030 CE): the breath simply follows the SI second.
- Not based on the day itself (Earth's rotation is irregular) - must be as good as SI.
- Rejected:
  - 7500000000 (fully round): day 77 s too short, drifts ~8 h/year.
  - 750E580000: drifts ~4.6 s (~1.1 breaths)/year, needs a leap breath nearly every year.
  - 750E583000: drifts ~0.31 s/year - acceptable, but no real benefit over exact.

# Length

**Decided:** the **pace** ≈ 1.4525 m, defined by **c = 2 × 10^7 paces per blink** (exact).

**Why:** a round speed of light gives an exact, SI-quality definition. The size is human: close to the
Roman pace (Latin passus, ~1.48 m), and 1000 paces ≈ a Roman mile.

Named sub-units (named because they're everyday sizes, like the inch and centimetre):

- **unc** = 1/10 pace (1/12 dec) ≈ 12.1 cm
- **dig** = 1/100 pace (1/144 dec) ≈ 1.01 cm

- Defined by the speed of light: **c = 2 × 10^7 paces per blink** (exact)
  - = 2 × 10^8 paces per breath = 859,963,392 (dec) per breath
  - (equivalently 2 × 10^10 paces per day)
- Light travels 2 × 10^8 paces in one breath ≈ 1,249,135 km (dec), about 3.25× the Earth-Moon distance
- 1000 paces = 2.51 km is literally a "thousand paces" (Latin mille passus = Roman mile)
- 15 triqua-paces ≈ 42.67 km ≈ a marathon (marathon = 14;98 triqua-paces)

Imperial comparisons:

| Imperial | Paces  | Uncs  | Digs  |
|----------|--------|-------|-------|
| 6 ft     | 1;313  | 13;13 | 131;3 |
| 1 ft     | 0;262  | 2;62  | 26;2  |
| 6 in     | 0;131  | 1;31  | 13;1  |
| 1 in     | 0;026  | 0;26  | 2;6   |

## Speed

- 100 km/h ≈ 67;82 paces/breath. Same digits at every scale because units step by twelve
  (≈ 6782;14 paces per 0;01 day, ≈ 67821;49 paces per 0;1 day)
- Speed signs in paces/breath; each 10 = 15.06 km/h (dec):

| Sign | km/h  | mph  | Use           |
|------|-------|------|---------------|
| 20   | 30.1  | 18.7 | school zone   |
| 30   | 45.2  | 28.1 | residential   |
| 40   | 60.2  | 37.4 | urban         |
| 50   | 75.3  | 46.8 | rural         |
| 60   | 90.4  | 56.1 | highway       |
| 70   | 105.4 | 65.5 | motorway      |
| 80   | 120.5 | 74.9 | fast motorway |

- Real limits needn't be round: like any changeover, existing values would be set to the nearest
  whole number rather than converted exactly. The nearest whole numbers land within 0.5 km/h:

| km/h now | Sign | km/h  |
|----------|------|-------|
| 40       | 28   | 40.2  |
| 50       | 34   | 50.2  |
| 60       | 40   | 60.2  |
| 70       | 48   | 70.3  |
| 80       | 54   | 80.3  |
| 90       | 60   | 90.4  |
| 100      | 68   | 100.4 |
| 110      | 74   | 110.4 |

**Decided:** real-world values (limits, products, standards) get rounded new values, not exact conversions.

**Why:** that's how every changeover works in practice (eg metric speed limits), and a whole number is easier to read.

## Gravity

- Would like g to be a nice dozenal number, but c and g have a fixed ratio (~2559X65 breaths), so only one can be exact.
- With c exact: g ≈ 0;9926 paces/blink² (≈ 99;26 paces/breath², 117.2 dec)
- g varies ~0.5% over Earth's surface anyway, so it's a poor basis for a definition.

# Mass

**Decided:** the **lib** ≈ 1.7714 kg, defined by fixing Planck's constant:
**h = 2;13 × 10^-28 exactly** (lib × pace² / blink) - same method SI has used since 2019 CE.
(= 2;13 × 10^-27 in lib × pace² / breath - same unit, just expressed per breath)

**Why:** fixing a constant is how SI defines mass since 2019 CE, so conversion is exact. The value of h was chosen so a cub of water ≈ 1 lib - the everyday rule of thumb matters more than a round constant.

- The value of h was chosen so a cube of water 1 unc per side (1 cub) ≈ 1 lib
  - water at 20 °C: 0.9994 (better than SI's 1 L of water = 0.9982 kg at 20 °C)
- Everyday rule of thumb works at every scale (1728 (dec) = 1000;):
  - 1 cub of water (12.1 cm side) ≈ 1 lib (1.77 kg)
  - 1 dig-cube of water (1.01 cm side) ≈ 1/1000 lib (≈ 1.03 g)
- 0;1 lib ≈ 147.6 g, 0;01 lib ≈ 12.3 g, 0;001 lib ≈ 1.025 g
- Converts exactly to kg (h is exact in SI too)
- Rejected:
  - Water itself as the definition: density depends on temperature, pressure, isotopes (SI dropped it for this reason)
  - 10^24 carbon-12 atoms (1.584 kg): nicely dozenal, but the dalton is not exact in SI
  - h = 2 × 10^-28 (1.864 kg): rounder h, but water cube only 0.95
- Priority used: c round > water ≈ 1 > h round. Normal people use c-based length and water; almost nobody uses h directly.

# Volume

**Decided:** the **cub** = a cube 1 unc per side ≈ 1.7736 L. Water in it ≈ 1 lib.

**Why:** volume follows directly from length (no separate definition), it makes the water rule of thumb
work, and dozenal fractions of it land close to common drink sizes.

Good size for milk. Dozenal fractions land close to common drink and pub sizes (all ~4% larger):

| Fraction   | mL   | Close to                                                |
|------------|------|---------------------------------------------------------|
| 1          | 1774 | large milk                                              |
| 0;8 (2/3)  | 1182 | pub jug (AU 1140)                                       |
| 0;6 (1/2)  | 887  |                                                         |
| 0;4 (1/3)  | 591  | pint (AU 570, UK 568); US 20 fl oz bottle (591) - exact |
| 0;3 (1/4)  | 443  | schooner (AU 425); 440 mL can                           |
| 0;2 (1/6)  | 296  | pot/middy (AU 285), UK half pint (284); 300 mL bottle   |
| 0;1 (a twelfth) | 148  | small glass / wine pour (150)                           |

Small volumes (kitchen and drinks):

| Fraction | mL   | Close to                                                            |
|----------|------|---------------------------------------------------------------------|
| 0;06     | 73.9 | quarter cup                                                         |
| 0;1      | 148  | half cup                                                            |
| 0;2      | 296  | cup (AU 250, US 237) - a bit larger                                 |
| 0;025    | 29.8 | spirit shot (30 mL)                                                 |
| 0;01     | 12.3 | standard drink of pure alcohol: 9.7 g ethanol (AU std drink = 10 g) |
| 0;004    | 4.1  | teaspoon (5 mL)                                                     |
| 0;001    | 1.03 | a dig-cube, about 1 mL / 1 g of water                               |

# Temperature

**Decided:** the **tep**, defined by fixing the Boltzmann constant **k = 2;07 × 10^-1E** (opus/tep), exact.

**Why:** 0 tep = freezing is what people actually need for weather and cooking (like Celsius). The size splits the gap between freezing and boiling into 100; equal steps (144 dec), so water
freezes at 0 °t and boils at 100 °t - the dozenal version of Celsius's 0 and 100.

- 1 tep = 0.694346 K (within 0.014% of 0;01 of the freezing-boiling gap)
- **0 tep = freezing** (273.15 K, same anchor as Celsius) - human focused; kelvin-style zero rejected
- Triple point of water (273.16 K = 0.01 °C) ≈ **0;021 °t**, not 0. Anchoring 0 °t at 273.15 K exactly, like
  Celsius, keeps 0 °t = 0 °C; the triple point has been a measured value (not exact) since SI's 2019 redefinition,
  so anchoring there would gain nothing
- boiling (sea level) ≈ EE;E9 tep, effectively 100 (144 dec). (SI's Celsius isn't exact either: 99.974 °C)
- 1 tep ≈ 0.694 °C ≈ 1.25 °F
- body temperature ≈ 45;35 tep, room temperature (21 °C) ≈ 26 tep
- absolute zero ≈ -289;48 tep (no nice ratio between absolute zero, freezing and boiling - fine)

# Electricity

**Decided:** fix the elementary charge **e = 1 × 10^-15 onus** exactly (12^-17 dec).

**Why:** a round fixed constant, exactly like SI; it makes the riv almost exactly an amp, and the alternatives were no better for common voltages.

- 1 onus (charge) ≈ 0.3555 C
- 1 riv (current, onus/blink) ≈ 1.0237 A - almost exactly an amp
- 1 imp (voltage, opus/onus) ≈ 87.21 V
- Common voltages aren't round (set by chemistry/history), but mains lines up:

| Voltage          | imp   | uncia-imp |
|------------------|-------|-----------|
| 1.5 V (AA)       | 0;026 | 0;26      |
| 5 V (USB)        | 0;083 | 0;83      |
| 12 V (car)       | 0;17X | 1;7X      |
| 24 V             | 0;338 | 3;38      |
| 120 V mains      | 1;462 | 14;62     |
| 230 V mains      | 2;779 | 27;79     |
| 240 V mains      | 2;903 | 29;03     |

- Rejected: e = 2 × 10^-15 (2.05 A, 43.6 V) or 0;6 × 10^-15 (0.51 A, 174 V) - no better for common voltages.

# Amount of substance

**Decided:** the **grex** = exactly **1;15 × 10^1X** entities (≈ 6.17235 × 10^23 dec).

**Why:** molar masses then come out ≈ atomic masses in 1/1000 lib, the same convenience chemists have with g/mol.

- Chosen so molar masses ≈ atomic masses in 1/1000 lib (like SI's g/mol): carbon-12 = 11.998, water = 18.01 (dec)
- Rejected: exactly 10^1X (5.52 × 10^23 dec) - rounder, but molar masses come out ×0.894;
  SI's Avogadro number - molar masses off by 2.5%

# Light

**Decided:** the **lam** = 1 candela (SI definition carried over: K_cd = 683 lm/W at 540 THz, dec).

**Why:** it's rarely used day to day, so there's nothing to gain from changing it.

- Rarely used day to day. Option later: rescale lam so K_cd is a round dozenal number per vig.

# Sound

**Decided:** sound level uses the **vox** (symbol **vo**): a dozenal log scale, 10 vox (twelve steps) for every
×12 in sound power, zero at the threshold of hearing (same reference as dB). 1 vox ≈ 0.90 dB.

**Why:** like dB, a level is a ratio, so it needs no Paludal units - but dB is built on log base 10, a decimal
leftover. A base-12 scale keeps the rules of thumb people use: ~1 step is the smallest audible change, and
**+10 vox is "twice as loud"** (10.8 dB; +10 dB today). Sound levels are everyday and regulated (noise limits,
headphone warnings), so converting is worth it. Name: Latin vox, voice; "son" rejected (the sone is a loudness unit).

- vox = 12 × log12(P / P0) for power; 24 × log12(p / p0) for sound pressure (p0 = 20 µPa)
- Like dB values today, everyday figures are rounded to the nearest 10

| Sound                       | dB now | Exact vox | Round vox |
|-----------------------------|--------|-----------|-----------|
| Threshold of hearing        | 0      | 0         | 0         |
| Whisper                     | 30     | 29        | 30        |
| Quiet room                  | 40     | 38        | 40        |
| Normal speech               | 60     | 57        | 60        |
| Busy traffic                | 70     | 66        | 70        |
| Hearing damage (8 h)        | 85     | 7E        | 80        |
| Concert                     | 100    | 93        | 90        |
| Pain                        | 120    | E1        | E0        |
| Jet at 30 m                 | 140    | 110       | 110       |

# Earthquakes

**Decided:** keep the moment magnitude scale (Mw) unchanged, just written in dozenal digits: M 7.5 = **M 7;6**.

**Why:** it's a log scale (no units needed), almost nobody does arithmetic with it, and every historical
record uses it. A base-12 version would change values by only ~7% - not worth breaking the records.

# Everyday reference

What things come to in the new units (3 significant digits). **Round** is the nearest round dozenal value
(whole, half, third or quarter, within 3%) - what a product, limit or setting would probably become.
Left blank for natural values (body temperature, speed of sound) and where the value is already round. Prefixes are used where the plain unit
gives awkward numbers: tc ÷1000, bc ÷100, uc ÷10, tq ×1000.

- tcli (1/1000 lib) ≈ 1.03 g and tccu (1 dig³) ≈ 1.03 mL - the new gram and millilitre
- tqp (1000 paces) ≈ 2.51 km; tqop (1000 opus) ≈ 53.6 kJ; tqpr (1000 pres) ≈ 17.5 kPa

## Length

| Thing | SI | Dozenal | Round |
|---|---|---|---|
| Credit card (long side) | 85.6 mm | 8;5X di | 8;6 di |
| A4 page (long side) | 297 mm | 2;55 un | 2;6 un |
| Adult height | 1.70 m | 1;21 p | 1;2 p |
| Tall person (6 ft) | 1.83 m | 1;31 p | 1;3 p |
| Door height | 2.04 m | 1;4X p | 1;5 p |
| Car length | 4.5 m | 3;12 p | 3;1 p |
| Cricket pitch | 20.12 m | 11;X p | (keeps 22 yd) |
| Olympic pool | 50 m | 2X;5 p | 30 p |
| 1 km | 1 km | 494 p |  |
| Marathon | 42.195 km | 14;X tqp | (keeps 42.195 km) |
| Sydney–Melbourne (straight line) | 713 km | 1E8 tqp |  |

## Races and sport

Exact conversions, and the round distance that would likely replace each one (rounded, not converted -
see Speed). Traditional distances tied to history (marathon, cricket pitch) keep their length.

| Distance now       | Exact            | Likely new distance | That is   |
|--------------------|------------------|---------------------|-----------|
| 25 m pool          | 15;3 p           | 16 p                | 26.1 m    |
| 50 m pool          | 2X;5 p           | 30 p                | 52.3 m    |
| 100 m sprint       | 58;X p           | 60 p                | 104.6 m   |
| 200 m              | E5;8 p           | 100 p               | 209.2 m   |
| 400 m (1 lap)      | 1XE;5 p          | 200 p (1 lap)       | 418.3 m   |
| 800 m              | 39X;9 p          | 400 p               | 836.7 m   |
| 1500 m / mile      | 720;8 p / 783;E p | 700 p              | 1464 m    |
| 5 km (parkrun)     | 1;EE tqp         | 2 tqp               | 5.02 km   |
| 10 km              | 3;EX tqp         | 4 tqp               | 10.04 km  |
| Half marathon      | 8;4X tqp         | keeps 21.1 km       |           |
| Marathon           | 14;99 tqp        | keeps 42.195 km     |           |
| Cricket pitch      | 11;X p           | keeps 22 yd         |           |

- The 100 m becomes the **60-pace sprint**; the 5 km and 10 km land almost exactly on 2 and 4 tqp

## Mass

| Thing | SI | Dozenal | Round |
|---|---|---|---|
| Egg | 60 g | 4X;6 tcli | 50 tcli |
| Apple | 150 g | 102 tcli | 100 tcli |
| 1 L of water | 1 kg | 0;693 li |  |
| Newborn baby | 3.5 kg | 1;E9 li | 2 li |
| Checked-in bag limit | 23 kg | 11 li |  |
| Adult | 75 kg | 36;4 li | 36 li |
| Small car | 1300 kg | 512 li | 500 li |

## Temperature

| Thing | SI | Dozenal | Round |
|---|---|---|---|
| Freezer | -18 °C | -21;E °t | -22 °t |
| Fridge | 4 °C | 5;92 °t | 5;8 °t |
| Cool day | 15 °C | 19;7 °t | 1X °t |
| Room | 21 °C | 26;3 °t | 26 °t |
| Warm day | 30 °C | 37;2 °t | 36 °t |
| Body | 37 °C | 45;3 °t |  |
| Heatwave | 45 °C | 54;X °t | 56 °t |
| Boiling water | 100 °C | 100 °t |  |
| Oven (moderate) | 180 °C | 197 °t | 1X0 °t |

## Volume

| Thing | SI | Dozenal | Round |
|---|---|---|---|
| Teaspoon | 5 mL | 4;X6 tccu | 5 tccu |
| Cup | 250 mL | 184 tccu | 180 tccu |
| Can of drink | 375 mL | 265 tccu | 260 tccu |
| Wine bottle | 750 mL | 0;50E cu | 0;5 cu |
| Milk bottle | 2 L | 1;16 cu | 1;2 cu |
| Bucket | 10 L | 5;78 cu | 5;6 cu |
| Car fuel tank | 50 L | 24;2 cu | 24 cu |
| Bath | 150 L | 70;7 cu | 70 cu |

## Time

| Thing | SI | Dozenal | Round |
|---|---|---|---|
| Heartbeat | 0.8 s | 0;93 be |  |
| Minute | 60 s | 1;25 mt |  |
| Hour | 60 min | 0;6 ch (60 mt) |  |
| Feature film | 2 h | 1 ch |  |
| Working day | 8 h | 4 ch |  |
| Night's sleep | 8 h | 4 ch |  |

## Speed

| Thing | SI | Dozenal | Round |
|---|---|---|---|
| Walking | 5 km/h | 3;EX p/br | 4 p/br |
| Cycling | 20 km/h | 13;E p/br | 14 p/br |
| School zone | 40 km/h | 27;X p/br | 28 p/br |
| Town | 50 km/h | 33;X p/br | 34 p/br |
| Motorway | 110 km/h | 73;8 p/br | 74 p/br |
| Airliner | 900 km/h | 4E9 p/br | 500 p/br |
| Sound | 343 m/s | 6X p/bl |  |

## Energy

| Thing | SI | Dozenal | Round |
|---|---|---|---|
| Apple (food energy) | 400 kJ | 7;57 tqop | 7;6 tqop |
| Daily food intake | 8700 kJ | 116 tqop | 120 tqop |
| Phone battery | 15 Wh | 1;01 tqop | 1 tqop |
| 1 kWh | 3.6 MJ | 57;2 tqop | 56 tqop |

## Power

| Thing | SI | Dozenal | Round |
|---|---|---|---|
| LED bulb | 10 W | 1;42 ucvg | 1;4 ucvg |
| Person at rest | 100 W | 1;15 vg |  |
| Kettle | 2400 W | 22;E vg | 23 vg |
| Small car engine | 100 kW | 794 vg | 800 vg |

## Pressure

| Thing | SI | Dozenal | Round |
|---|---|---|---|
| Atmosphere | 101.3 kPa | 5;97 tqpr |  |
| Car tyre (gauge) | 220 kPa | 10;7 tqpr | 11 tqpr |

## Voltage

| Thing | SI | Dozenal | Round |
|---|---|---|---|
| AA battery | 1.5 V | 2;59 bcim | 2;6 bcim |
| USB | 5 V | 8;31 bcim | 8;6 bcim |
| Car battery | 12 V | 17;X bcim | 18 bcim |
| Mains (AU) | 230 V | 2;78 im | 2;8 im |

Notes:
- Temperatures, heights, speeds and voltages come out in comfortable numbers
- Energy and pressure need the tq prefix for everyday sizes (opus and pres are small); food labels in tqop
- A feature film is 1 chime; a working day and a night's sleep are 4 chimes each

# Imperial conversions

Both directions. Dozenal-side values are dozenal; imperial-side values are decimal (as imperial is used now).
UK and US units differ for volume and tons.

| Quantity | Imperial          | = dozenal units          | Dozenal unit = imperial (dec)  |
|----------|-------------------|--------------------------|--------------------------------|
| Length   | 1 inch            | 2;627 di                 | 1 di = 0.3971 in               |
| Length   | 1 foot            | 2;627 un                 | 1 un = 0.3971 ft (4.765 in)    |
| Length   | 1 yard            | 0;767X p                 | 1 p = 1.589 yd (4.765 ft)      |
| Length   | 1 mile            | 783;E p (0;784 tqp)      | 1 tqp = 1.560 mi               |
| Length   | 1 nautical mile   | 8X3 p                    | 1 tqp = 1.355 nmi              |
| Mass     | 1 ounce           | 2;37X bcli               | 1 bcli = 0.4339 oz             |
| Mass     | 1 pound           | 0;30X6 li                | 1 li = 3.905 lb                |
| Mass     | 1 stone           | 3;703 li                 | 1 li = 0.2790 st               |
| Mass     | 1 ton (UK long)   | 3E9;7 li                 |                                |
| Mass     | 1 ton (US short)  | 368;1 li                 |                                |
| Volume   | 1 fl oz (UK)      | 23;82 tccu               | 1 tccu = 0.03612 fl oz (UK)    |
| Volume   | 1 fl oz (US)      | 24;99 tccu               | 1 tccu = 0.03471 fl oz (US)    |
| Volume   | 1 pint (UK)       | 0;3X18 cu                | 1 cu = 3.121 pt (UK)           |
| Volume   | 1 pint (US)       | 0;325 cu                 | 1 cu = 3.748 pt (US)           |
| Volume   | 1 gallon (UK)     | 2;691 cu                 | 1 cu = 0.3901 gal (UK)         |
| Volume   | 1 gallon (US)     | 2;174 cu                 | 1 cu = 0.4685 gal (US)         |
| Speed    | 1 mph             | 1;348 p/br               | 1 p/br = 0.7798 mph            |
| Energy   | 1 Calorie (kcal)  | E2;E op                  | 1 tqop = 12.80 kcal            |
| Energy   | 1 BTU             | 2X;05 op                 | 1 op = 0.02938 BTU             |
| Power    | 1 horsepower      | 8;429 vg                 | 1 vg = 0.1197 hp               |
| Pressure | 1 psi             | 0;4897 tqpr              | 1 tqpr = 2.535 psi             |

- Inch → dig and foot → unc give the same digits (2;627), because both systems step by twelve there
- The name links too: Latin *uncia* (a twelfth) is the root of both inch (1/12 foot) and ounce (1/12 Roman pound)

## Fahrenheit

°t = (°F - 32) × 0.8001 (decimal arithmetic, then convert) - so roughly **(°F - 32) × 4/5**.

| °F    | °t     | |
|-------|--------|-|
| 0     | -21;7  | |
| 32    | 0      | freezing |
| 50    | 12;5   | |
| 68    | 24;X   | room |
| 98.6  | 45;3   | body |
| 100   | 46;5   | |
| 212   | 100    | boiling |
| 350   | 192    | oven |

# Names

**Decided:** short names (3-4 letters preferred), Latin roots where possible, no clash with existing everyday
words or units, and no object or container names.

**Why:** short names are quick to say and write; Latin roots echo older measures (pace, uncia, libra) and work
across languages; clashes cause confusion when both systems are in use.

| Quantity               | Name  | Symbol | Size (SI)           | Named after                                       | English relatives            |
|------------------------|-------|--------|---------------------|---------------------------------------------------|------------------------------|
| Time (base)            | blink | bl     | 0.3472 s            | English: the blink of an eye                      |                              |
| Time (≈ second)        | beat  | be     | 1.0417 s            | English: a heartbeat                              |                              |
| Time (clock)           | breath | br    | 4.1667 s            | English: one breath                               |                              |
| Time (dozenal hour)    | chime | ch     | 2 h exactly         | English: clocks chime on the hour                 |                              |
| Time (dozenal minute)  | moment | mt    | 50 s exactly        | Latin momentum, movement; medieval moment = 90 s  | moment, momentum             |
| Length (base)          | pace  | p      | 1.4525 m            | Latin passus, a pace (Roman pace ≈ 1.48 m)        | pace, passage                |
| 1/10 pace              | unc   | un     | ≈ 12.1 cm           | Latin uncia, a twelfth                            | inch, ounce                  |
| 1/100 pace             | dig   | di     | ≈ 1.01 cm           | Latin digitus, finger (Roman digit ≈ 1.85 cm)     | digit                        |
| Mass                   | lib   | li     | ≈ 1.7714 kg         | Latin libra, pound; also scales (Roman pound)     | lb (pound), Libra            |
| Volume (unc cube)      | cub   | cu     | 1.7736 L            | Latin cubus, cube                                 | cube, cubic                  |
| Temperature            | tep   | °t     | 0.694 K/°C          | Latin tepor, warmth                               | tepid                        |
| Force                  | vis   | vi     | ≈ 21.3 N            | Latin vis, force, strength                        | vim                          |
| Energy                 | opus  | op     | ≈ 31.0 J            | Latin opus, work                                  | opus, operate                |
| Power                  | vig   | vg     | ≈ 89.3 W            | Latin vigor, liveliness, energy                   | vigour, vigorous             |
| Pressure               | pres  | pr     | ≈ 10.1 Pa           | Latin pressus, pressed                            | press, pressure              |
| Current                | riv   | ri     | ≈ 1.024 A           | Latin rivus, a stream                             | rivulet, derive              |
| Charge                 | onus  | on     | ≈ 0.3555 C          | Latin onus, load, burden                          | onus, onerous                |
| Voltage                | imp   | im     | ≈ 87.21 V           | Latin impetus, push, rush                         | impetus, impetuous           |
| Amount of substance    | grex  | gx     | 6.17 × 10^23 things | Latin grex, flock, herd                           | gregarious, congregate       |
| Luminous intensity     | lam   | la     | 1 cd                | Latin lampas, lamp, torch                         | lamp                         |
| Sound level            | vox   | vo     | ≈ 0.90 dB per vox   | Latin vox, voice                                  | voice, vocal                 |

- Rejected: heft, jug (object names), pond (sounds like a lake), mass/vol (clash with quantity names / "% vol"),
  hand (clashes with horse hand 10.16 cm), nail, inc (too close to "inch"), lux/lum (existing SI units),
  cal (calorie), pot (container), erg (CGS unit), grad (gradian), mol (mole)

# Prefixes

**Decided:** use SDN (Systematic Dozenal Nomenclature, Dozenal Society of America).

**Why:** it's an existing standard, it's systematic (prefixes are built from digit names, not memorised), and it extends to any power. Roots for X and E were changed to dek / el to match the spoken digits.

Digit roots: 0 nil, 1 un, 2 bi, 3 tri, 4 quad, 5 pent, 6 hex, 7 sept, 8 oct, 9 enn, X dek, E el
(SDN's own roots for X and E are dec and lev; changed to match the spoken digit names)

- multiply by 10^n: root(s) + **-qua**  (unqua- ×10, biqua- ×100, triqua- ×1000, ... unnilqua- ×10^10)
- divide by 10^n:   root(s) + **-cia**  (uncia- ÷10, bicia- ÷100, tricia- ÷1000, ...)
- uncia = Latin "a twelfth" (origin of inch and ounce)
- Common sizes also get short everyday names (unc = uncia-pace, dig = bicia-pace)
- Prefix symbols: see Symbols

# Prior art

- **TGM** (Tom Pendlebury): Tim = 1/10^4 hour ≈ 0.1736 s (= half a blink exactly), Grafut ≈ 29.6 cm (from gravity),
  Maz ≈ 25.8 kg (water cube). Earth-based (hour + gravity), so less rigorous than this system;
  length and mass have no clean relation to ours.
- **SDN** (DSA): the prefix system adopted above. Inspired by Pendlebury's TGM prefixes.
- **Primel** metrology: base time 1/10^6 day (= 0;01 breath), length unit ≈ 8.2 mm, uses an SDN variant.
- **Do-Gro-Mo** (early DSA): do = 12, gro = 144, mo = 1728 (dec). Adopted for spoken numbers, extended with bimo / trimo.

# Open items / next steps

- Write the spec up as a proper document (LaTeX, Markdown or AsciiDoc)
- Give short names to a few everyday multiples (food energy tqop, pressure tqpr) instead of changing the
  coherent derived units (proposed, not decided)
- Holocene Era: record why it was chosen
- A body-rhythm name for the chime (2 h) to match blink / beat / breath? (sleep cycle is ~1.5-2 h)
- Standard sizes: food energy labels (opus), paper sizes, clothing/shoe sizes
- Review existing dozenal clock designs (https://clocks.dozenal.ca)
- Optional: rescale lam for a round K_cd
