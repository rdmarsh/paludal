package main

import (
	"math"
	"strings"
)

// A clock face drawn with braille characters (each cell is 2×4 dots).
// Paludal dials have 0 at the bottom, 6 (noon) at the top, and turn clockwise.

const (
	colChime  = "\x1b[1;33m" // bold yellow
	colMoment = "\x1b[1;36m" // bold cyan
	colBreath = "\x1b[31m"   // red
	colDial   = "\x1b[2m"    // dim
	colReset  = "\x1b[0m"
)

type canvas struct {
	cols, rows int
	dots       [][]uint8  // braille bits per cell
	colour     [][]string // colour per cell (last hand drawn wins)
	text       [][]rune   // characters that replace the braille cell
}

func newCanvas(rows int) *canvas {
	c := &canvas{cols: rows * 2, rows: rows}
	c.dots = make([][]uint8, rows)
	c.colour = make([][]string, rows)
	c.text = make([][]rune, rows)
	for y := range rows {
		c.dots[y] = make([]uint8, c.cols)
		c.colour[y] = make([]string, c.cols)
		c.text[y] = make([]rune, c.cols)
	}
	return c
}

// set turns on the dot at (x, y) in dot coordinates.
func (c *canvas) set(x, y float64, colour string) {
	xi, yi := int(math.Round(x)), int(math.Round(y))
	cx, cy := xi/2, yi/4
	if xi < 0 || yi < 0 || cx >= c.cols || cy >= c.rows {
		return
	}
	bits := [4][2]uint8{{0x01, 0x08}, {0x02, 0x10}, {0x04, 0x20}, {0x40, 0x80}}
	c.dots[cy][cx] |= bits[yi%4][xi%2]
	if colour != "" {
		c.colour[cy][cx] = colour
	}
}

// point returns the dot position for a fraction of a turn at a radius.
// 0 is straight down, and the hand turns clockwise (down → left → up → right).
func (c *canvas) point(turn, radius float64) (float64, float64) {
	cx, cy := float64(c.cols), float64(c.rows*2) // centre, in dots
	a := 2 * math.Pi * turn
	return cx - radius*math.Sin(a), cy + radius*math.Cos(a)
}

func (c *canvas) line(turn, from, to float64, colour string) {
	for r := from; r <= to; r += 0.5 {
		x, y := c.point(turn, r)
		c.set(x, y, colour)
	}
}

func (c *canvas) label(turn, radius float64, ch rune) {
	x, y := c.point(turn, radius)
	cx, cy := int(math.Round(x))/2, int(math.Round(y))/4
	if cx >= 0 && cy >= 0 && cx < c.cols && cy < c.rows {
		c.text[cy][cx] = ch
	}
}

func (c *canvas) String() string {
	var b strings.Builder
	for y := range c.rows {
		for x := range c.cols {
			switch {
			case c.text[y][x] != 0:
				b.WriteString(colDial + string(c.text[y][x]) + colReset)
			case c.dots[y][x] != 0:
				b.WriteString(c.colour[y][x] + string(rune(0x2800+int(c.dots[y][x]))) + colReset)
			default:
				b.WriteByte(' ')
			}
		}
		b.WriteString("\x1b[K\n")
	}
	return b.String()
}

// drawFace draws the dial and four hands for blink n of the day.
func drawFace(rows int, n int64) string {
	c := newCanvas(rows)
	r := float64(rows*2) - 7 // dial radius in dots, leaving room for the numbers

	// Dial: outline, 12 marks, numbers.
	for i := range 360 {
		x, y := c.point(float64(i)/360, r)
		c.set(x, y, colDial)
	}
	for m := range 12 {
		c.line(float64(m)/12, r-2.5, r, colDial)
		c.label(float64(m)/12, r+4.5, rune(digits[m]))
	}

	const blinksPerChime = blinksPerDay / 12 // 10000 (doz)
	const blinksPerMoment = blinksPerChime / 144
	chime := float64(n) / blinksPerDay                   // whole day
	moment := float64(n%blinksPerChime) / blinksPerChime // sweeps smoothly
	breath := float64(n%blinksPerMoment/12) / 12         // steps once per breath, onto a mark
	beat := float64(n%blinksPerMoment/3) / 48            // steps once per beat, 4 per mark

	c.line(beat, 0, r-1, colDial) // drawn first, so the coloured hands win where they overlap
	c.line(breath, 0, r-3, colBreath)
	c.line(moment, 0, r*0.85, colMoment)
	c.line(chime, 0, r*0.55, colChime)
	return c.String()
}
