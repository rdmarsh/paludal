## Hexadecimal

Proposed (not decided): when written alongside dozenal, hexadecimal (base 16, used in computing) keeps
X and E for ten and eleven, and the four digits after them take the next letters, A B C D. This **dozenal hex**
counts 0-9 X E A B C D.

**Why:** X and E then mean the same thing in both bases, so nobody has to remember that hex E is fourteen
while dozenal E is eleven. A B C D are free, because dozenal uses no other letters.

**Advantage:** one set of digits covers both bases: dozenal is 0-E, and hex is the same digits plus four.

| Binary | Standard hex | Dozenal hex | Dozenal | Decimal |
|--------|--------------|-------------|---------|---------|
| 0000   | 0            | 0           | 0       | 0       |
| 0001   | 1            | 1           | 1       | 1       |
| 0010   | 2            | 2           | 2       | 2       |
| 0011   | 3            | 3           | 3       | 3       |
| 0100   | 4            | 4           | 4       | 4       |
| 0101   | 5            | 5           | 5       | 5       |
| 0110   | 6            | 6           | 6       | 6       |
| 0111   | 7            | 7           | 7       | 7       |
| 1000   | 8            | 8           | 8       | 8       |
| 1001   | 9            | 9           | 9       | 9       |
| 1010   | A            | X           | X       | 10      |
| 1011   | B            | E           | E       | 11      |
| 1100   | C            | A           | 10      | 12      |
| 1101   | D            | B           | 11      | 13      |
| 1110   | E            | C           | 12      | 14      |
| 1111   | F            | D           | 13      | 15      |

- Watch: in standard hex A-D mean ten to thirteen, but here they mean twelve to fifteen. Mark which is meant
  (standard hex keeps its 0x prefix) wherever both could appear
- Every hex (and binary) fraction ends in dozenal: 100 (144 dec) is 0x90, a multiple of 0x10 (16 dec), so
  each hex place needs at most two dozenal places (0x0.1 = 0;09)
- Not the other way: thirds repeat in hex, as they do in binary and decimal. Quarters are the common ground:
  0x0.4 = 0;3 = 0.25 (dec)
