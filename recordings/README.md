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
| `2026-10-27-0926-f21-trunk-flexion-unlabelled` | F2.1 Trunk Flexion | **Purpose not recorded.** Not reps and not a hard-stop excursion — strokes climb 166 → 169 → 227 → 317 → 381mm through the recording. Refused |
| `2026-10-27-0929-f21-trunk-flexion-unlabelled` | F2.1 Trunk Flexion | **Purpose not recorded.** Four irregular strokes, 45–231mm. Refused |
| `2026-10-30-2221-f21-trunk-flexion-hole3` | F2.1 Trunk Flexion | Range-limiting pin at **hole 3**. Nothing else recorded. Refused: reads 66mm per rep against 206mm for hole 3 on 27 October, and the trace is dominated by a 20Hz ringing that decays over 1-2s after each knock — the mount, not the lifting |
| `2026-10-30-2228-b1-leg-extension` | B1 Leg Extension | The coach's words: **getting "crap scores for really decent form"**, and long holds at the loaded ends being penalised. Scored 80 on the 8 October build and 65 on 27 October; the drop traced to scoring changes, not the lift. This is the set the 1 November hold change was made for |

## Baseline, build 1 November 2026

What the current build makes of each one, with **no machine selected**, at a 4-2-4-2 target and
the form's default allowances. With no machine selected a long hold is now free at both ends;
only an end a machine marks REST is judged on the long side, so picking such a machine can
lower a score. Phase figures are mean seconds. Regenerate this table whenever the
segmentation changes — a silent shift in any row is the thing most worth catching.

The 1 November build changed three things, and every row moved because of the first:
holds now begin when the stack is nearly still (10% of typical peak speed, was 5%), the hold
allowance is 25% (was 15% in the form), and a long hold costs nothing unless the machine marks
that end REST. Holds read 0.1-0.5s longer and strokes correspondingly shorter. The deliberately
bad control moves 26 → 29; the good sets of 6 and 20 October move into the 83-94 range.

One refusal is lost by the change and should not be read as a pass:
`10-27-0929-f21-trunk-flexion-unlabelled` sat on the 30% stroke-spread line and now falls just
under it. It is four irregular strokes of unknown purpose, as labelled above.

| Recording | Reps | TUT | Score | Trusted | Lift | Top | Lower | Btm | Travel | Spread | Refused for |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `10-04-0141-trial` | 4 | 33.8s | 68 | yes | 2.32 | 1.87 | 2.79 | 1.96 | 285mm | 13% | — |
| `10-05-1151-unlabelled` | 8 | 93.7s | 86 | yes | 4.47 | 1.31 | 4.60 | 1.37 | 172mm | 22% | — |
| `10-05-2021-unlabelled` | 8 | 92.4s | 83 | yes | 4.09 | 2.29 | 4.27 | 1.65 | 257mm | 16% | — |
| `10-06-0425-matched-1` | 6 | 70.2s | 94 | yes | 3.63 | 2.43 | 4.17 | 1.76 | 260mm | 12% | — |
| `10-06-0427-matched-2` | 7 | 76.4s | 83 | yes | 3.55 | 2.57 | 4.32 | 1.46 | 238mm | 13% | — |
| `10-06-0430-matched-3` | 8 | 92.3s | 93 | yes | 3.75 | 2.42 | 4.00 | 1.57 | 256mm | 8% | — |
| `10-06-0431-deliberately-bad` | 10 | 61.4s | 29 | yes | 2.18 | 0.53 | 2.30 | 1.83 | 234mm | 25% | — |
| `10-06-0751-g5-neck-extension` | 4 | 52.5s | 44 | **NO** | 2.18 | 1.92 | 3.17 | 1.16 | 17mm | 26% | stack moved only 19mm per rep |
| `10-06-0755-b6-leg-press-fast` | 3 | 88.6s | 67 | **NO** | 7.61 | 1.23 | 11.53 | 2.30 | 209mm | 14% | concentric and eccentric travel disagree by 25%; 1 merged phase(s) |
| `10-06-0817-c7-row` | 9 | 69.3s | 44 | yes | 2.33 | 1.41 | 3.19 | 0.42 | 254mm | 16% | — |
| `10-08-2024-f21-trunk-flexion` | 11 | 61.0s | 21 | **NO** | 2.50 | 0.46 | 2.46 | 0.76 | 169mm | 38% | stroke travel varied by 38% |
| `10-08-2028-pulldown-light` | 9 | 65.6s | 49 | yes | 2.82 | 0.97 | 3.38 | 0.73 | 261mm | 10% | — |
| `10-08-2030-pulldown-light` | 4 | 45.5s | 93 | yes | 3.27 | 2.53 | 4.16 | 2.23 | 258mm | 9% | — |
| `10-16-2109-c3-pulldown-loaded` | 10 | 91.0s | 59 | yes | 3.34 | 0.97 | 4.63 | 0.94 | 232mm | 14% | — |
| `10-16-2119-h1-curl` | 6 | 65.3s | 65 | **NO** | 3.65 | 1.51 | 4.78 | 1.10 | 196mm | 81% | stroke travel varied by 81% |
| `10-20-0851-clock-paced-1` | 9 | 102.8s | 89 | yes | 4.15 | 1.72 | 4.68 | 1.34 | 139mm | 18% | — |
| `10-20-0855-clock-paced-2` | 9 | 99.6s | 87 | yes | 4.50 | 1.64 | 4.22 | 1.15 | 152mm | 4% | — |
| `10-20-0858-clock-paced-3-failure` | 10 | 107.6s | 55 | **NO** | 4.34 | 0.72 | 4.11 | 2.20 | 178mm | 44% | stroke travel varied by 44% |
| `10-20-0911-clock-paced-4` | 7 | 74.6s | 90 | yes | 3.48 | 1.91 | 4.01 | 1.65 | 255mm | 9% | — |
| `10-20-0917-clock-paced-5` | 7 | 77.3s | 90 | yes | 4.29 | 1.33 | 3.85 | 2.44 | 134mm | 11% | — |
| `10-23-2113-h1-curl-failure` | 7 | 71.5s | 88 | yes | 3.22 | 1.83 | 3.67 | 2.23 | 259mm | 19% | — |
| `10-27-0910-f21-trunk-flexion-hole3` | 7 | 84.1s | 90 | yes | 4.62 | 1.64 | 4.60 | 1.35 | 206mm | 6% | — |
| `10-27-0916-f21-trunk-flexion-hole2` | 7 | 82.3s | 85 | yes | 3.98 | 1.99 | 4.49 | 1.66 | 121mm | 14% | — |
| `10-27-0926-f21-trunk-flexion-unlabelled` | 3 | 29.6s | 65 | **NO** | 3.91 | 3.25 | 2.66 | 1.27 | 179mm | 41% | stroke travel varied by 41%; concentric and eccentric travel disagree by 36% |
| `10-27-0929-f21-trunk-flexion-unlabelled` | 4 | 39.0s | 64 | yes | 2.78 | 1.66 | 3.80 | 1.39 | 156mm | 30% | — |
| `10-30-2221-f21-trunk-flexion-hole3` | 8 | 81.9s | 44 | **NO** | 2.57 | 1.37 | 2.92 | 1.26 | 95mm | 127% | stack moved only 66mm per rep; stroke travel varied by 127%; concentric and eccentric travel disagree by 27% |
| `10-30-2228-b1-leg-extension` | 7 | 77.6s | 86 | yes | 4.54 | 1.94 | 4.22 | 1.16 | 276mm | 21% | — |

Eight of twenty-seven are refused. That is the app declining to put four tidy phase numbers on a
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

## A claim withdrawn: nothing here shows a stroke to be impossible

The October F2.1 recording contains a 431mm stroke against a 195mm median, and that was
written up — in a commit message and in conversation — as "an impossible 431mm stroke",
offered as the clearest case for wanting a machine ceiling.

It should not have been. **Calling a reading impossible requires knowing what the machine can
travel, and that has never been measured on any machine here.** What the 431mm figure actually
showed was a stroke far out of step with the rest of its own set, which is what the stroke-spread
check already catches, and which is why that set is refused. The refusal was right. The reason
given for it was not, and "impossible" claimed a measurement that does not exist.

A second observation made it worth re-reading. The unlabelled recording of 27 October 09:26
reads a 381mm stroke on the same machine. That recording is refused too, so 381mm is not a
trustworthy distance either — it cannot establish a ceiling any more than 431mm could refute
one. But two refused recordings reading 381mm and 431mm on a machine whose travel nobody has
measured is not a basis for calling either one impossible.

The ceiling check is still worth building, and `maxStackTravelMm` is still the measurement that
would make it possible. Until that field holds a number, every stroke in this directory is
judged only against the other strokes beside it.

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
