# Recordings

Every real accelerometer recording the app has been tested against, as exported by the app
itself, with whatever the coach said about each one at the time.

The CSVs are the cheap part. The labels are not: a set is only useful for checking the score
or the fatigue rule if someone recorded what actually happened in it, and that can only be
captured at the time. Those notes previously existed nowhere but a chat log. They are below.

Two columns, `t_ms` and `magnitude` — elapsed milliseconds and the magnitude of the raw
acceleration vector in m/s². That is the whole input. Filenames carry the recording's own
timestamp from the export.

## What is labelled, and what is not

Read the label column as the coach's own words, not as ground truth. **Where a cell says
"not recorded", nothing is known** — do not substitute a guess from the filename or from a
neighbouring row. In particular:

- **No set has a machine confirmed per recording** except where the code appears in the
  filename. The 20 October sets were described as including the chest press, but not which.
- **No set has video or frame-by-frame timing.** Phase-timing accuracy has never been checked
  against a real lift; the figures quoted elsewhere come from synthetic strokes.
- **One set has a blind coach mark** (16 Oct, 6–7 out of 10, given before the score was seen).
  Every other score comparison would be after the fact and is therefore worthless for
  calibration.
- **Three sets carry a failure label.** That is the entire labelled basis of the fatigue rule.
- One lifter, one operator, one handset, throughout. Nothing here speaks to another body, a
  different lifting style, or another phone's sensor.

| Recording | Machine | What the coach said |
|---|---|---|
| `2026-10-04-0141-trial` | not recorded | A loosely controlled early trial, not held to a tempo |
| `2026-10-05-1151-unlabelled` | not recorded | Nothing recorded |
| `2026-10-05-2021-unlabelled` | not recorded | Nothing recorded. Never analysed until 23 October |
| `2026-10-06-0425-matched-1` | not recorded | First of three sets recorded back to back on one machine, prescribed 4-2-4-2 |
| `2026-10-06-0427-matched-2` | not recorded | Second of the three |
| `2026-10-06-0430-matched-3` | not recorded | Third of the three |
| `2026-10-06-0431-deliberately-bad` | not recorded, same machine as the three above | Recorded deliberately badly — fast, no holds — as a control, straight after them |
| `2026-10-06-0751-g5-neck-extension` | G5 Neck Extension | — |
| `2026-10-06-0755-b6-leg-press-fast` | B6 Leg Press | Run deliberately fast, to imitate how clients actually lift rather than how they are prescribed |
| `2026-10-06-0817-c7-row` | C7 Row | — |
| `2026-10-08-2024-f21-trunk-flexion` | F2.1 Trunk Flexion | — |
| `2026-10-08-2028-pulldown-light` | pulldown, light load | — |
| `2026-10-08-2030-pulldown-light` | pulldown, light load | — |
| `2026-10-16-2109-c3-pulldown-loaded` | C3 Pulldown | **Taken to or near failure.** First set recorded at a working load. **Marked 6–7 out of 10 by the coach before the score was shown.** An entry aid was used to bring the handles within reach (opening stroke 151mm) and an exit aid to catch the stack at the end (closing stroke 133mm), against a 244mm median |
| `2026-10-16-2119-h1-curl` | H1 Curl | Nothing recorded at the time |
| `2026-10-20-0851-clock-paced-1` | not recorded | One of five sets that morning. **The lifter paced against a clock, trying to hold the prescribed tempo.** The chest press (D6) was among the machines used, and entry/exit aids were used on it |
| `2026-10-20-0855-clock-paced-2` | not recorded | As above |
| `2026-10-20-0858-clock-paced-3-failure` | not recorded | As above, and **"I reached muscular failure."** Opens with roughly 45s of setup; the app refuses the full recording and only reads it cropped to the lifting |
| `2026-10-20-0911-clock-paced-4` | not recorded | Uploaded without comment |
| `2026-10-20-0917-clock-paced-5` | not recorded | Uploaded without comment |
| `2026-10-23-2113-h1-curl-failure` | H1 Curl, both arms | **Muscular failure.** The final rep was **a failed rep** — the coach confirmed they could not complete the range, rather than it being an exit aid or setting the stack down. It reads 109mm up and 103mm down against a 266mm median. Whether the mount differed from the 16 October curl set is not recalled |
| `2026-10-27-0910-f21-trunk-flexion-hole3` | F2.1 Trunk Flexion | Range-limiting pin at **hole 3**. One of a pair recorded six minutes apart on one machine, differing only in the pin |
| `2026-10-27-0916-f21-trunk-flexion-hole2` | F2.1 Trunk Flexion | Range-limiting pin at **hole 2**, the restricted setting. The pair with the set above |

## Baseline, build 23 October 2026

What the current build makes of each one, with **no machine selected**, at a 4-2-4-2 target.
No machine selected means both holds are judged in both directions; picking a machine whose
ends are LOADED makes a long hold free and lifts the score a point or two. Phase figures are
mean seconds. Regenerate this table whenever the segmentation changes — a silent shift in any
row is the thing most worth catching.

| Recording | Reps | TUT | Score | Trusted | Lift | Top | Lower | Btm | Travel | Spread | Refused for |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `10-04-0141-trial` | 4 | 34.4s | 68 | yes | 2.65 | 1.69 | 2.93 | 1.78 | 288mm | 12% | — |
| `10-05-1151-unlabelled` | 8 | 94.3s | 71 | yes | 4.54 | 1.14 | 5.08 | 1.34 | 174mm | 7% | — |
| `10-05-2021-unlabelled` | 8 | 92.7s | 74 | yes | 4.42 | 2.20 | 4.59 | 1.33 | 257mm | 16% | — |
| `10-06-0425-matched-1` | 6 | 70.4s | 80 | yes | 3.93 | 2.00 | 4.58 | 1.46 | 263mm | 12% | — |
| `10-06-0427-matched-2` | 7 | 76.4s | 75 | yes | 3.94 | 2.11 | 4.50 | 1.22 | 239mm | 13% | — |
| `10-06-0430-matched-3` | 8 | 92.6s | 80 | yes | 4.06 | 1.99 | 4.39 | 1.29 | 258mm | 7% | — |
| `10-06-0431-deliberately-bad` | 10 | 61.6s | 26 | yes | 2.38 | 0.38 | 2.54 | 1.66 | 237mm | 25% | — |
| `10-06-0751-g5-neck-extension` | 4 | 52.5s | 37 | **NO** | 2.19 | 1.92 | 3.18 | 1.15 | 17mm | 26% | stack moved only 19mm per rep |
| `10-06-0755-b6-leg-press-fast` | 3 | 89.5s | 45 | **NO** | 8.19 | 1.19 | 12.06 | 1.67 | 211mm | 13% | lift/lower travel disagree by 24%; 1 merged phase |
| `10-06-0817-c7-row` | 9 | 69.3s | 42 | yes | 2.50 | 1.50 | 3.52 | — | 254mm | 16% | — |
| `10-08-2024-f21-trunk-flexion` | 11 | 61.1s | 23 | **NO** | 2.77 | 0.33 | 2.54 | 0.95 | 181mm | 37% | stroke travel varied by 37% |
| `10-08-2028-pulldown-light` | 9 | 66.0s | 42 | yes | 2.92 | 0.87 | 3.72 | 0.76 | 262mm | 9% | — |
| `10-08-2030-pulldown-light` | 3 | 35.3s | 91 | yes | 3.53 | 2.36 | 4.48 | 2.01 | 259mm | 10% | — |
| `10-16-2109-c3-pulldown-loaded` | 10 | 91.0s | 54 | yes | 3.60 | 0.96 | 4.94 | 0.97 | 236mm | 11% | — (reads as near failure) |
| `10-16-2119-h1-curl` | 6 | 65.4s | 38 | **NO** | 2.82 | 1.25 | 5.03 | 0.83 | 139mm | 87% | stroke travel varied by 87%; lift/lower disagree by 24% |
| `10-20-0851-clock-paced-1` | 9 | 103.1s | 68 | yes | 4.46 | 1.31 | 5.03 | 1.01 | 139mm | 19% | — |
| `10-20-0855-clock-paced-2` | 9 | 99.8s | 70 | yes | 4.77 | 1.42 | 4.53 | 0.88 | 152mm | 5% | — |
| `10-20-0858-clock-paced-3-failure` | 10 | 107.6s | 47 | **NO** | 4.53 | 0.87 | 4.20 | 1.69 | 183mm | 44% | stroke travel varied by 44% (the setup, see above) |
| `10-20-0911-clock-paced-4` | 7 | 74.6s | 78 | yes | 3.76 | 1.63 | 4.30 | 1.34 | 256mm | 9% | — |
| `10-20-0917-clock-paced-5` | 7 | 77.6s | 71 | yes | 4.71 | 1.16 | 4.33 | 2.17 | 134mm | 13% | — |
| `10-23-2113-h1-curl-failure` | 7 | 72.3s | 89 | yes | 3.60 | 1.50 | 3.95 | 2.04 | 263mm | 18% | — |
| `10-27-0910-f21-trunk-flexion-hole3` | 7 | 85.0s | 73 | yes | 4.88 | 1.59 | 4.94 | 1.10 | 207mm | 7% | — |
| `10-27-0916-f21-trunk-flexion-hole2` | 7 | 82.8s | 71 | yes | 4.56 | 1.86 | 4.96 | 1.30 | 123mm | 15% | — |

Five of twenty-three are refused. That is the app declining to put four tidy phase numbers on a
recording it cannot stand behind, which is the behaviour it was built for — not a failure rate.

## Two corrections this directory exists to prevent

Both were found by checksumming the originals rather than trusting the notes kept alongside
them, which is why the files are now here under their own timestamps.

- **The refused curl set is from 16 October, not 6 October.** It had been discussed as a
  6 October recording. Its content matches the 16 October 21:19 export, ten minutes after the
  loaded pulldown. So the gap between it and the clean 23 October curl is one week, not two
  and a half.
- **The 6 October row recording was uploaded five times** under three different timestamps —
  08:17:00, 08:17:37 and 08:17:42 — all byte-identical. One copy had been kept separately as a
  "bicep" set and treated as independent evidence. There is no separate bicep recording from
  that morning; there is one recording, counted once here.

## The pin pair, and what it settles

The two recordings of 27 October are the only controlled travel comparison here. One machine,
one lifter, one mount, six minutes apart, same prescribed tempo — the only thing changed was
the range-limiting pin, hole 3 then hole 2. Everything else in this directory varies the
machine or the day along with the stroke, so nothing else isolates stroke length.

**It settles whether short travel costs you turnarounds: it does not.** The restricted set,
at 123mm, holds three turnarounds at 2.0s exactly — dead on prescription — and runs straight
through three others, which the app reports as no pause at all:

| rep | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| hold at top | none | none | 1.4s | 2.0s | 2.0s | none | 2.0s |

A reading that could not resolve a turnaround at 123mm could not have resolved those three.
So the missing ones are missing because they were not held. This is a stronger argument than
the corpus-wide one, which only shows that the sets with the most missing turnarounds are also
the ones with the longest strokes — the seated row loses 65% of its turnarounds at 254mm,
while the 263mm curl of 23 October loses none.

The pair also makes a prediction worth testing. 207mm at hole 3 and 123mm at hole 2 is 84mm of
carrier travel per hole, so **hole 4 should read about 291mm** — a 40% step, far larger than
anything the reading's scatter could produce. It is not a clean test on its own, because it
assumes the holes are evenly spaced and the linkage linear; a miss would not say which of the
three assumptions failed. Running the hard-stop excursion at each hole, with a tape, converts
it into one: the pin is the hard stop for its setting, so three settings give three known
distances spanning better than 2:1 on a single machine.

## What is still missing

In the order that would help most:

1. **One set filmed side-on to the stack**, which settles two things at once. Footage of the
   D6 chest press on 24 October showed the plate labels are legible at phone resolution from
   several feet away — the main stack runs 240, 260 … 540 in 20-unit steps, one per plate, with
   a fine 2–20 stack above it. So a video of a real set gives phase boundaries frame by frame
   *and* stack travel read straight off the plates the carrier passes, tied to the exact set
   the app scored rather than to a separate measurement. Shoot it square to the stack with the
   whole travel in frame and a clap or tap to sync.
2. **Blind coach marks.** One set has one. Ten would make the score comparison quotable. The
   mark has to be written down before the score is seen, every time.
3. **Measured stack travel on the remaining machines** — `maxStackTravelMm` in `machines.json`
   is null on all 26. A tape, hard stop to hard stop, is still the quick way to cover machines
   nobody is going to film.
4. **More failure labels**, and ideally the lifter's own pacing intent alongside them. The
   fatigue rule fires on one of the three labelled failure sets, and both misses are sets where
   the lift got *faster* across the reps because the lifter was pacing to a clock.
