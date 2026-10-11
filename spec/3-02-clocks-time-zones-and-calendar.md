## Clocks, time zones and calendar

The time units themselves are in Part 2 (Time).

### Analogue clocks

**Decided:** a 24-hour dial with twelve marks, noon at the top, turning clockwise.

**Why:** one turn per day shows the whole day at a glance; noon at the top matches the sun at its highest,
and clockwise keeps the convention people already know.
The design, and the idea of splitting the day by twelve, then twelve, then twelve as the basis of Paludal time,
came from Paul Rapoport's Diurnal 1 clock (https://clocks.dozenal.ca).

**Advantage:** the whole day is visible at once, and the hand follows the sun.

**Decided:** four hands, each turning twelve times faster than the one before, so each hand shows one digit
of the time: at E91;7 they point at E, 9, 1 and 7. The hands are named after the digit they show: **hand 1**
to **hand 4** (said "hand two", not "second hand").

**Why:** with one hand per digit the time reads straight off the hands, every hand reads the same twelve
marks, and the clock is the same as Paul Rapoport's Diurnal 1 (prior art adopted). The earlier design had a
chime, moment and breath hand plus a beat hand: the moment hand showed two digits against 144 fine marks, and
the breath hand turned 144 times faster than it, not twelve. Hour, minute and second hand don't fit four
dozenal hands, and "second hand" already means something else. The beat hand was dropped: it shows no digit
and adds clutter (clocks.dozenal.ca leaves out a fifth hand for the same reason).

**Advantage:** the time is read off the hands digit by digit, on the same dial as an existing dozenal clock.

| Hand   | Turns once per        | Shows                   | At E91;7 | Like        |
|--------|-----------------------|-------------------------|----------|-------------|
| Hand 1 | day                   | chime                   | E        | hour hand   |
| Hand 2 | chime (2 h)           | dozens of moments       | 9        |             |
| Hand 3 | 10 moments (10 min)   | moments                 | 1        | minute hand |
| Hand 4 | moment (50 s)         | breath                  | 7        | second hand |

![The clock at E91;7 (about 23:31): hand 1 just before 0, hand 2 just past 9, hand 3 half way from 1 to 2, hand 4 on 7.](figures/clock.svg)

- Hand 1 is short and wide, hands 2 and 3 longer and thinner, hand 4 thin and coloured, like a second hand
- Hand 4 steps once per breath, landing on each mark, so it always points at the breath digit.
  It once stepped once per beat (4 steps per mark), but then it looked like a beat hand
- 144 (dec) fine marks between the twelve are optional (clocks.dozenal.ca calls them bicia-marks)
- **Noon (600) points straight up, midnight (000) straight down**
  - dawn ≈ 300 on the left, dusk ≈ 900 on the right (at the equinoxes)
  - **Clockwise everywhere** (bottom → left → top → right), both hemispheres - matches convention,
    and clocks are clockwise because they copied northern sundials
  - matches the sun's path when facing south in the northern hemisphere, so a correctly
    oriented clock roughly agrees with a sundial
- **The clock as a compass** (rough): the sun's bearing in turns is about the time of day - north (000) at
  midnight, east (300) at dawn, south (600) at noon, west (900) at dusk. So:
  - northern hemisphere: lay the clock face up and point hand 1 at the sun; 0 points north and 6 south
  - southern hemisphere (where the sun moves the other way, through the north): point 6 at the sun; hand 1
    points north
  - it is only rough: clocks keep zone time, not sun time (up to 30 moments, half an hour, apart in most
    zones, another 60 with daylight saving), and the sun's bearing doesn't change evenly, least of all in the tropics near noon.
    The 12-hour watch trick (south is half way between the hour hand and 12) has the same limits
- Compared with the clocks at https://clocks.dozenal.ca (Paul Rapoport; reviewed 2026 CE): Paludal's clock
  is their **Diurnal 1** - one turn a day ("diurnal", Latin *diurnus*, daily), 0 (midnight) at the bottom,
  6 (noon) at the top, each hand twelve times faster than the next. Their readout (E51.E4) is the time
  format adopted, with a semicolon. Their other dials:
  - **Diurnal 2**: 0 (midnight) at the top, noon at the bottom - the same way up as a compass
  - **Diurnal 3**: 0 at the top, but the day counted from noon, so 0 is noon (as astronomers counted days
    until 1925 CE, and Julian Day numbers still do)
  - **Semidiurnal**: the slow hand turns twice a day, like am / pm, with dozenal hands below it
  - **Signed** versions of each, which count down to the next mark after half way (as "twenty to eight" does)
  - Their hand names are SDN place values on a hidden unit of 0;001 day, which is our moment:
    **unqua-hand** (×10 moments, our hand 2), **nilqua-hand** (×1 moment, hand 3) and **uncia-hand**
    (÷10 moment = a breath, hand 4); the slowest hand has no name. Nilqua could as well be nilcia, since
    10^0 is 1 either way. Not adopted: they only work once the moment is taken as the unit, and uncia is
    close to our unc

### Daylight saving and time zones

**Decided:** no daylight saving, for now.

**Why:** a 1-hour shift is half a chime (60 moments), which changes the moment digits (645 becomes 6X5).
Shifting a whole chime (2 h) is too big a jump. Neither is good, and places half a chime apart (eg NSW and
Queensland in summer) are annoying to deal with. Dropping it puts NSW and Queensland on the same time all year.

**Advantage:** the clock never jumps, and neighbouring places stay on the same time all year.

**Decided (for now):** keep today's 24 time zones, based on UTC (London is +0). Neighbouring zones are half a
chime (1 hour) apart, so offsets are whole or half chimes; a few places keep their quarter-hour offsets.
To review later.

**Why:** twelve whole-chime zones would probably be too few.

**Advantage:** today's zones and offsets carry over unchanged.

Standard time (no daylight saving):

| City | UTC now (standard time) | Paludal (moments) | Local time when London is 600 (noon) |
|---|---|---|---|
| Honolulu | UTC-10 | UTC-500 | 100 |
| Anchorage | UTC-9 | UTC-460 | 160 |
| Los Angeles, Vancouver | UTC-8 | UTC-400 | 200 |
| Denver | UTC-7 | UTC-360 | 260 |
| Chicago, Mexico City | UTC-6 | UTC-300 | 300 |
| New York, Toronto | UTC-5 | UTC-260 | 360 |
| Santiago | UTC-4 | UTC-200 | 400 |
| São Paulo, Buenos Aires | UTC-3 | UTC-160 | 460 |
| London, Reykjavik | UTC | UTC | 600 |
| Paris, Berlin, Rome | UTC+1 | UTC+060 | 660 |
| Cairo, Johannesburg | UTC+2 | UTC+100 | 700 |
| Moscow, Istanbul | UTC+3 | UTC+160 | 760 |
| Dubai | UTC+4 | UTC+200 | 800 |
| Karachi | UTC+5 | UTC+260 | 860 |
| Delhi, Mumbai | UTC+5:30 | UTC+290 | 890 |
| Kathmandu | UTC+5:45 | UTC+2X6 | 8X6 |
| Dhaka | UTC+6 | UTC+300 | 900 |
| Bangkok, Jakarta | UTC+7 | UTC+360 | 960 |
| Beijing, Singapore, Perth | UTC+8 | UTC+400 | X00 |
| Tokyo, Seoul | UTC+9 | UTC+460 | X60 |
| Adelaide, Darwin | UTC+9:30 | UTC+490 | X90 |
| Sydney, Melbourne, Brisbane | UTC+10 | UTC+500 | E00 |
| Auckland | UTC+12 | UTC+600 | 000 (next day) |

### Years

**Decided:** years are counted in the **Dozenal Holocene** (DH) era of the Dozenal Holocene calendar: year 0
began in 9565 BCE, so for dates from 1 January on, **DH year = CE year + 9563 (dec)**. 2026 CE = **6859 DH**.
The year still starts on 1 January.

**Why:** a dozenal system shouldn't start its count at 10,000 BCE: that's only a round number in decimal
(5,954 in dozenal). Adopt prior art instead: the Dozenal Holocene calendar (Paul Rapoport and Sanketh Kolhar)
already counts years in dozenal from the start of the Holocene, and its start has an astronomical reason -
around 9564 BCE the Earth was last nearest the Sun on the northern summer solstice. Replaces the earlier
Human (Holocene) Era (Emiliani's, 1 HE = 10,000 BCE, which made 2026 CE 6E62 HE). "DH" rather than "HE",
because HE already means Emiliani's count.

**Advantage:** the year count shares an origin with existing dozenal calendars, has a reason other than a
decimal round number, and keeps every year of recorded history positive.

- 2026 CE = 11,589 (dec) = **6859 DH**. A BCE year n is 9564 - n (dec) DH
- New Year stays on 1 January (the Gregorian months are kept, see Calendar). The Dozenal Holocene calendar
  itself starts its year at the December solstice (about 21 December UTC), so between the solstice and
  31 December its year number is already one higher. If that calendar is ever adopted, New Year moves with it
- Spoken as two pairs, like "twenty twenty-six" (that's how years are said now): 6859 = "six do eight, five do
  nine"
  - round years: 7000 = "seven mo", 6900 = "six do nine gro"

### Calendar

**Decided:** keep the standard Gregorian months and 7-day weeks. Only the numbering changes:
**week numbers** (ISO weeks) are written in dozenal: week 1 to 44 (52 dec), 45 in long years (53 dec).

**Why:** 365 (dec) days can't be split into dozenal-round months, and changing the 7-day week is too big a change. Writing the numbers in dozenal keeps the whole system consistent.

**Advantage:** dates and weeks stay as people know them; only the digits change.

- eg 3 Oct 2026 CE is week 34 (ISO week 40 dec)

**Decided:** keep the month names January to December (Jan to Dec). In all-number dates the month is its
dozenal number: October is X, November E, December 10 (eg 6859-X-03).

**Why:** the names were briefly replaced by the SDN digit roots (Un, Bi, Tri ... Sept, Oct, Enn, Dek, El, Do),
which fixed the Roman misnumbering (September to December were the seventh to tenth months when the year began
in March). But Sept and Oct already mean September and October, so "3 Oct" became ambiguous - a permanent
confusion, worse than the old misnumbering. Rejected: SDN roots (that clash); Greek roots (mono, di, tri,
tetra ... octa, ennea, deca), which shorten to Oct and Dec and clash the same way; a -men suffix (Latin
mensis), which reads as English "men" (Hexmen, Septmen).

**Advantage:** no month name can be mistaken for another, and dates read as they do today.

**Decided:** months are numbered from 1 (January 1 to December 10), not from 0.

**Why:** numbering from 0 (January 0, December E) would fit every month in one digit, but it is confusing:
month 3 would be April. Dates name a day or month (the 3rd, the tenth month), so they count from 1; a time
of day measures how much of the day has passed, so it counts from 0. Days of the month would otherwise have to
start at 0 too, and computing already shows the trap: JavaScript numbers months 0 to 11, a well-known source
of bugs. Fixed-width dates use two digits for the month anyway (6859-0X-03, as 2026-01-03 today), so
nothing is lost.

**Advantage:** month numbers mean what they always have; only December's is written differently (10).

**Day of month (decided):** written in dozenal, 1 to 27 (31 dec).

**Why:** every number in the system is dozenal; a date shouldn't mix bases.

**Advantage:** a date is written in one base, like every other number.

- eg 3 Oct 2026 CE = 3 Oct 6859; 31 (dec) Oct = 27 Oct; Christmas = 21 Dec

**Possibility (not decided):** the Dozenal Holocene calendar (Paul Rapoport, with Sanketh Kolhar;
https://clocks.dozenal.ca/pdf/dozenal-calendar.pdf): twelve months of 30 (dec) days, each of five 6-day weeks
("stretches"), with the 5-6 leftover "S-days" outside any month but spread through the year so the months
keep in step with the seasons. The year starts on a solstice or equinox (the December solstice by default)
instead of 1 January, so leap years follow the Sun rather than a divide-by-4 rule. Months are numbered (or
named after the zodiac in Greek), and the six days are named after colours (Ruber, Arantius, Flāvus, Viridis,
Cæruleus, Purpureus).
- A 6-day week would mean a 4-day working week with the usual 2-day weekend
- For now, the 7-day week stays: changing it is too big a change, and 365 (dec) days can't be split evenly anyway
