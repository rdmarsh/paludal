## Log scales

Levels and scales that are ratios, so they need no Paludal units.

### Sound

**Decided:** sound level uses the **vox** (symbol **vo**): a dozenal log scale, 10 vox (twelve steps) for every
×12 in sound power, zero at the threshold of hearing (same reference as dB). 1 vox ≈ 0.90 dB.

**Why:** like dB, a level is a ratio, so it needs no Paludal units - but dB is built on log base 10, a decimal
leftover. A base-12 scale keeps the rules of thumb people use: ~1 step is the smallest audible change, and
**+10 vox is "twice as loud"** (10.8 dB; +10 dB today). Sound levels are everyday and regulated (noise limits,
headphone warnings), so converting is worth it. Name: Latin vox, voice; "son" rejected (the sone is a loudness unit).

**Advantage:** sound levels keep the rules of thumb people know (+10 is twice as loud), without a decimal log.

All numbers here are dozenal, so a level can be worked out without going through decimal:

- **vox = 10 × log₁₂(P / P₀)** for power or intensity, and **20 × log₁₂(p / p₀)** for sound pressure
  (pressure is squared to give power, so its factor doubles, as dB uses 10 and 20)
- References (the same physical levels as dB, so the scales line up exactly): p₀ = 20 µPa = 5;XX × 10^-6 pr,
  and P₀ = 10^-12 W/m² (dec) = 2;64 × 10^-11 vg/p²
- From a dB figure: vox = dB × 1;141 (first write the dB value in dozenal)
- Rules of thumb:
  - +1 vox is about the smallest change you can hear
  - **+10 vox** is ten (twelve dec) times the power, and sounds about twice as loud
  - two equal sources together: **+3;4 vox** (like +3 dB)
  - twice as far from the source: **-6;8 vox** (like -6 dB)
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

### Earthquakes

**Decided:** keep the moment magnitude scale (Mw) unchanged, just written in dozenal digits: M 7.5 = **M 7;6**.

**Why:** it's a log scale (no units needed), almost nobody does arithmetic with it, and every historical
record uses it. A base-12 version would change values by only ~7% - not worth breaking the records.

**Advantage:** every historical record stays valid; only the digits change.

### Acidity (pH)

**Decided:** replace pH with an acidity scale where **0 is neutral, acids are positive and bases negative**.

**Why:** if the system is being changed anyway, it may as well be done right. pH runs backwards (lower =
more acidic) and centres on 7, which is only neutral at 25 °C. Replaces the earlier decision to keep pH
unchanged in dozenal digits.

**Advantage:** a higher number means more acidic, and 0 always means neutral.

**Decided:** the scale is called **acidity** (eg lemon juice is acidity +4;5), and
**acidity = log base 12 of ([H+] / [H+] in pure water at the same temperature)**.

**Why:** it's the simplest formula that gets it right: nothing needs converting (more H+ than pure water
gives a positive number, less a negative one, pure water 0), and each step is twelve times. Rejected:
log 12 of [H+]/[OH-] (the same information with every number doubled) and 7 - pH (keeps base-ten steps,
and 0 is only neutral at 25 °C). The word acidity already means acid content in wine and food (in g/L),
but that's not a serious clash. So

**Advantage:** it needs no concentration unit, and neutral is 0 at every temperature.

- 0 is neutral at **every** temperature (pH's neutral point is 7.47 at 0 °C, 7 at 25 °C, 6.8 at body
  temperature and 6.14 at 100 °C)
- each step of 1 is 10 (12 dec) times more acidic
- it's a ratio of two concentrations, so it needs no concentration unit (no mol/L vs grex/cub problem)
- From a pH reading (25 °C): write the pH in dozenal, then **acidity = (7 - pH) × 0;E15** (0;E15 is log₁₂ 10,
  so the whole sum is dozenal). Everyday values run from about +6;6 to -6;6
- Measured directly: a glass-electrode meter (which every pH meter is) gives a voltage that changes by
  **1;32 bcim per step of acidity** at 25 °C, so a Paludal meter reads acidity with no pH in between

| Substance | pH (dec) | Acidity (log 12) | log 12 of [H+]/[OH-] | 7 - pH (log 10) |
|---|---|---|---|---|
| Battery acid | 0.8 | +5;9 | +E;6 | +6;2 |
| Stomach acid | 1.5 | +5;1 | +X;2 | +5;6 |
| Lemon juice | 2.2 | +4;5 | +8;E | +4;X |
| Cola | 2.5 | +4;2 | +8;4 | +4;6 |
| Vinegar | 2.9 | +3;X | +7;7 | +4;1 |
| Orange juice | 3.5 | +3;3 | +6;6 | +3;6 |
| Tomato | 4.3 | +2;6 | +5;0 | +2;8 |
| Black coffee | 5.0 | +1;X | +3;8 | +2;0 |
| Clean rain | 5.6 | +1;4 | +2;7 | +1;5 |
| Milk | 6.6 | +0;4 | +0;9 | +0;5 |
| Pure water | 7.0 | 0 | 0 | 0 |
| Blood | 7.4 | -0;4 | -0;9 | -0;5 |
| Sea water | 8.1 | -1;0 | -2;0 | -1;1 |
| Baking soda | 8.3 | -1;2 | -2;5 | -1;4 |
| Soap | 10.0 | -2;9 | -5;7 | -3;0 |
| Household ammonia | 11.6 | -4;3 | -8;6 | -4;7 |
| Bleach | 12.5 | -5;1 | -X;2 | -5;6 |
| Drain cleaner (lye) | 14.0 | -6;6 | -11;0 | -7;0 |

- Values at 25 °C, in dozenal digits. The three columns are three ways to build the scale:
  - **Acidity (log 12)**, chosen: compares H+ with pure water. Each step is 12 times more acidic
  - **log 12 of [H+]/[OH-]**: compares acid (H+) with base (OH-). As one rises the other falls, so the
    ratio moves twice as fast and every number is doubled. Same information, bigger numbers
  - **7 - pH**: today's pH flipped and shifted. Steps are still ×10 (dec), and 0 is only neutral at 25 °C
- No hard bounds: strong acids go above +6;6 and strong alkalis below -6;6, as pH goes below 0 and above
  14. Superacids are measured on other scales (Hammett, down to about -25 pH)
- Chemists' buffer maths keeps its shape: pH = pKa + log(base/acid) becomes
  acidity = Ka-acidity - log₁₂(base/acid), where Ka-acidity = (7 - pKa) × 0;E15 (pKa in dozenal), a one-off
  conversion of old tables
- Converting old pH readings needs the temperature, because neutral moves with it
