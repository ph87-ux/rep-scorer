# Travel calibration fixtures

The app's stroke travel is a double integration of a gravity-magnitude signal, so it has no
reference to check itself against on a real machine. These two scripts generate recordings
whose stroke distance is known exactly, which gives it one.

Each stroke is a half-cosine acceleration profile, `a(t) = A·cos(πt/T)` with
`A = π²·s / (2T²)`. That integrates to velocity zero at both ends and a displacement of
exactly `s`, so the generated set has a stroke length that is true by construction rather
than by measurement.

- `amp.js` — sixteen strokes at each of 150mm, 220mm and 300mm, carrying vertical noise at
  the level a real mount produces. Run it, load each CSV into the app, compare.
- `rect.js` — two otherwise identical 300mm sets, one whose transverse noise rises while the
  stack moves and one whose does not. Written to test whether a rattling stack inflates
  travel through the magnitude's rectification term. It does not: the two read alike.

## Result, 17 October 2026

| true stroke | app reads | error | per-stroke range |
|---|---|---|---|
| 150mm | 148.1mm | −1.3% | 106–174mm |
| 220mm | 214.5mm | −2.5% | 174–240mm |
| 300mm | 290.8mm | −3.1% | 249–317mm |

The reconstruction has no systematic over-read, and what bias it has is conservative. The
average over a set is good to about 3%; a single stroke is worth about ±15%, so no one rep's
distance should be read as precise.

This matters for one open question. The lat pulldown was taped at roughly 220mm and the app
reads 236–262mm on it, which the evidence summary reported as the app reading high. On the
figures above a 220mm carrier reads back at about 215mm, so the disagreement is not in the
reconstruction. Either the tape figure is wrong, or it measured a part that does not travel
with the phone — a cable ratio between the stack and the carrier would produce exactly this.
Re-measure the machine before calibrating anything away.
