# muscle-overlay

Superimposes anatomical muscle-activation highlights onto exercise photos and
short videos. Detects body-joint positions with MediaPipe Pose, then draws
semi-transparent capsule shapes (quads, glutes, chest, lats, etc.) anchored to
those joints — bright/pulsing for the primary muscles of the given exercise,
dim/static for secondary ones — and composites them back onto the source with
ffmpeg.

## Setup

```bash
cd muscle-overlay
uv sync            # or: pip install -e .
# ffmpeg + ffprobe must be on PATH
```

## Usage

```bash
# Still image
uv run python render_overlay.py --input squat.jpg --exercise squat -o squat_overlay.png

# Short video (works well up to at least ~30-60s clips)
uv run python render_overlay.py --input squat.mp4 --exercise squat -o squat_overlay.mp4

# Faster preview render (720p)
uv run python render_overlay.py -i clip.mp4 -e deadlift -o preview.mp4 --preview

# Run pose detection on every frame instead of every 2nd (slower, smoother)
uv run python render_overlay.py -i clip.mp4 -e bench_press -o out.mp4 --sample-every 1
```

Run `python render_overlay.py --help` for the full list of supported
`--exercise` values (`muscle_data.EXERCISES`).

## How it works

1. `pose_extract.py` runs MediaPipe Pose per frame (video) or once (image),
   returning pixel-space joint positions.
2. `geometry.py` turns a muscle-region spec + joint positions into a capsule
   polygon — a segment between two joints, offset and thickened to sit
   roughly where that muscle is.
3. `muscle_data.py` maps each exercise to primary/secondary muscles and
   defines each muscle's region (which joints, which offset/width).
4. `render_overlay.py` draws the capsules onto a transparent RGBA layer per
   frame, encodes that to an alpha-channel `.mov` (`qtrle`), and uses ffmpeg's
   `overlay` filter to composite it back onto the original — same
   PTS-shifted-overlay approach as the `video-use` skill.

## Notes / limitations

- Front vs. back muscles (e.g. quads vs. hamstrings) can't be told apart from
  a single 2D camera view, so the "front/back" offset is a visual
  approximation, not a true anatomical projection — good enough for
  "roughly where that muscle is," not for a medical-grade illustration.
- No person detected in a frame → that frame's overlay is skipped (video) or
  the run fails with a clear error (image).
- Add exercises/muscles by editing `muscle_data.py`; no other file needs to
  change for a straightforward addition.

## Demo

`demo_synthetic.py` renders the overlay against a hand-built stick figure
(no real footage needed) — useful for eyeballing capsule geometry after
tuning `muscle_data.py`.
