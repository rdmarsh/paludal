// blinker sounds the blink, beat and breath, in step with Paludal time of day.
//
//	go run .                  sound every beat (≈ 1.04 s) and breath (≈ 4.17 s)
//	go run . -from=blink      also click every blink (≈ 0.35 s)
//	go run . -from=breath     breaths only
//	go run . -bell            terminal bell on breaths instead of generated tones
//	go run . -face=false      digital time only, no clock face
//	go run . -size=16         clock face height in terminal rows
package main

import (
	"encoding/binary"
	"flag"
	"fmt"
	"math"
	"os"
	"os/signal"
	"time"

	"github.com/ebitengine/oto/v3"
)

const (
	// 1 blink = 25/72 s exactly; 1 beat = 3 blinks; 1 breath = 10 (doz) blinks.
	blinkNanos   = int64(25 * time.Second / 72)
	blinksPerDay = 12 * 12 * 12 * 12 * 12 // 100000 (doz)
	digits       = "0123456789XE"
	rate         = 44100
)

type tone struct {
	freq   float64
	length time.Duration
	volume float64
}

var (
	blinkTone  = tone{1800, 15 * time.Millisecond, 0.2}
	beatTone   = tone{1200, 40 * time.Millisecond, 0.4}
	breathTone = tone{880, 120 * time.Millisecond, 0.6}
)

func main() {
	from := flag.String("from", "beat", "smallest unit to sound: blink, beat or breath")
	bell := flag.Bool("bell", false, "use the terminal bell on breaths instead of generated tones")
	face := flag.Bool("face", true, "draw a clock face")
	size := flag.Int("size", 21, "clock face height in terminal rows")
	flag.Parse()

	every, ok := map[string]int64{"blink": 1, "beat": 3, "breath": 12}[*from]
	if !ok {
		fmt.Fprintln(os.Stderr, "-from must be blink, beat or breath")
		os.Exit(2)
	}

	if !*bell {
		if err := startAudio(every); err != nil {
			fmt.Fprintln(os.Stderr, "no audio, using terminal bell:", err)
			*bell = true
		}
	}

	if *face {
		fmt.Print("\x1b[2J\x1b[?25l") // clear screen, hide cursor
		stop := make(chan os.Signal, 1)
		signal.Notify(stop, os.Interrupt)
		go func() {
			<-stop
			fmt.Print("\x1b[?25h\n") // show cursor again
			os.Exit(0)
		}()
	} else {
		fmt.Println("Paludal time: chime;moments breath (blink dimmed). Ctrl-C to stop.")
	}
	for {
		n, at := nextBlink(time.Now())
		time.Sleep(time.Until(at))
		if *face {
			fmt.Printf("\x1b[H%s\n%*s%s\x1b[K\n\n  %schime%s  %smoment%s  %sbreath%s  (0 at the bottom, noon at the top)\x1b[K",
				drawFace(*size, n), *size-3, "", format(n),
				colChime, colReset, colMoment, colReset, colBreath, colReset)
		} else {
			fmt.Printf("\r  %s  ", format(n))
		}
		if *bell && n%12 == 0 {
			fmt.Print("\a")
		}
	}
}

// nextBlink returns the number of the next blink since local midnight and when it starts.
// Boundaries are computed from midnight each time, so the beat never drifts.
func nextBlink(now time.Time) (int64, time.Time) {
	midnight := midnightOf(now)
	n := now.Sub(midnight).Nanoseconds()/blinkNanos + 1
	return n % blinksPerDay, midnight.Add(time.Duration(n * blinkNanos))
}

func midnightOf(t time.Time) time.Time {
	return time.Date(t.Year(), t.Month(), t.Day(), 0, 0, 0, 0, t.Location())
}

// format writes a blink count as time of day: chime, semicolon, two moment digits and the
// breath, eg E;917, followed by the blink digit dimmed (extra precision, like tenths of a second).
func format(n int64) string {
	var d [5]byte
	for i := 4; i >= 0; i-- {
		d[i] = digits[n%12]
		n /= 12
	}
	return fmt.Sprintf("%c;%s\x1b[2m%c\x1b[0m", d[0], d[1:4], d[4])
}

// startAudio opens one continuous audio stream. Beeps are synthesised straight into it at the
// sample where each blink starts, so there's no per-beep start-up delay.
func startAudio(every int64) error {
	ctx, ready, err := oto.NewContext(&oto.NewContextOptions{
		SampleRate:   rate,
		ChannelCount: 1,
		Format:       oto.FormatSignedInt16LE,
		BufferSize:   20 * time.Millisecond,
	})
	if err != nil {
		return err
	}
	<-ready
	now := time.Now()
	s := &stream{every: every, start: now.Sub(midnightOf(now)).Nanoseconds()}
	p := ctx.NewPlayer(s)
	p.Play()
	go func() { // keep the player referenced for the life of the program
		for {
			time.Sleep(time.Hour)
			_ = p.IsPlaying()
		}
	}()
	return nil
}

// stream is an io.Reader producing 16-bit mono samples. Sample i plays at start + i/rate
// (nanoseconds since midnight), give or take the small output buffer.
type stream struct {
	every int64
	start int64
	i     int64
}

func (s *stream) Read(buf []byte) (int, error) {
	n := len(buf) / 2
	for k := 0; k < n; k++ {
		t := s.start + s.i*int64(time.Second)/rate
		s.i++
		b := t / blinkNanos
		offset := time.Duration(t - b*blinkNanos)

		var v float64
		switch {
		case b%12 == 0:
			v = breathTone.sample(offset)
		case b%3 == 0 && s.every <= 3:
			v = beatTone.sample(offset)
		case s.every == 1:
			v = blinkTone.sample(offset)
		}
		binary.LittleEndian.PutUint16(buf[2*k:], uint16(int16(v*math.MaxInt16)))
	}
	return n * 2, nil
}

// sample returns the tone's value at time offset after it starts (0 once it has finished).
func (t tone) sample(offset time.Duration) float64 {
	if offset >= t.length {
		return 0
	}
	fade := math.Min(1, (t.length-offset).Seconds()/0.005) // 5 ms fade-out avoids a click
	return t.volume * fade * math.Sin(2*math.Pi*t.freq*offset.Seconds())
}
