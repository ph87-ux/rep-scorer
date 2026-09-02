#!/usr/bin/env python3
"""Superimpose anatomical muscle-activation highlights onto an exercise
photo or short video.

Usage:
    python render_overlay.py --input squat.mp4 --exercise squat -o out.mp4
    python render_overlay.py --input calf_raise.jpg --exercise calf_raise -o out.png
"""
import argparse
import math
import os
import shutil
import subprocess
import sys
import tempfile

from PIL import Image, ImageDraw

from geometry import region_capsule, torso_scale
from muscle_data import EXERCISES, MUSCLE_REGIONS, MUSCLE_COLORS
import pose_extract

ROLE_ALPHA = {"primary": 175, "secondary": 90}
PULSE_AMPLITUDE = 35
PULSE_HZ = 0.9


def draw_muscle(draw, capsule, color, alpha):
    rect, cap1, cap2 = capsule
    fill = (*color, alpha)
    if rect is not None:
        draw.polygon(rect, fill=fill)
    if cap1 is not None:
        cx, cy, r = cap1
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill)
    if cap2 is not None:
        cx, cy, r = cap2
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill)


def build_overlay_frame(w, h, landmarks, muscle_roles, t_seconds):
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer, "RGBA")
    if landmarks is None:
        return layer
    scale = torso_scale(landmarks)
    pulse = math.sin(2 * math.pi * PULSE_HZ * t_seconds)

    # secondary muscles first (background), primary last (on top / most visible)
    draw_order = sorted(muscle_roles.items(), key=lambda kv: kv[1] == "primary")
    for muscle, role in draw_order:
        spec = MUSCLE_REGIONS[muscle]
        color = MUSCLE_COLORS[muscle]
        base_alpha = ROLE_ALPHA[role]
        alpha = max(0, min(255, int(base_alpha + (PULSE_AMPLITUDE if role == "primary" else 0) * pulse)))
        for side in spec["sides"]:
            capsule = region_capsule(landmarks, spec, side, scale)
            if capsule is None:
                continue
            draw_muscle(draw, capsule, color, alpha)
    return layer


def roles_for(exercise):
    ex = EXERCISES[exercise]
    roles = {}
    for m in ex["primary"]:
        roles[m] = "primary"
    for m in ex["secondary"]:
        roles.setdefault(m, "secondary")
    return roles


def render_image(input_path, exercise, out_path):
    w, h, landmarks = pose_extract.extract_image(input_path)
    if landmarks is None:
        print("No person detected in the image.", file=sys.stderr)
        sys.exit(1)
    base = Image.open(input_path).convert("RGBA")
    overlay = build_overlay_frame(w, h, landmarks, roles_for(exercise), t_seconds=0.0)
    out = Image.alpha_composite(base, overlay)
    out.convert("RGB").save(out_path)
    print(f"wrote {out_path}")


def render_video(input_path, exercise, out_path, sample_every, preview):
    roles = roles_for(exercise)
    tmp_dir = tempfile.mkdtemp(prefix="muscle_overlay_")
    frames_dir = os.path.join(tmp_dir, "frames")
    os.makedirs(frames_dir, exist_ok=True)

    gen = pose_extract.extract_video(input_path, sample_every=sample_every)
    n_written = 0
    for i, landmarks in gen:
        meta = pose_extract.extract_video.meta if hasattr(pose_extract.extract_video, "meta") else None
        w = meta["width"] if meta else None
        h = meta["height"] if meta else None
        fps = meta["fps"] if meta else 30.0
        if w is None:
            continue
        t = i / fps
        frame = build_overlay_frame(w, h, landmarks, roles, t_seconds=t)
        frame.save(os.path.join(frames_dir, f"{i:06d}.png"))
        n_written += 1

    meta = pose_extract.extract_video.meta
    fps = meta["fps"]

    overlay_video = os.path.join(tmp_dir, "overlay.mov")
    subprocess.run([
        "ffmpeg", "-y", "-framerate", str(fps), "-i", os.path.join(frames_dir, "%06d.png"),
        "-c:v", "qtrle", overlay_video,
    ], check=True, capture_output=True)

    scale_filter = "scale=1280:-2" if preview else "scale=1080:-2"
    filter_complex = (
        f"[0:v]{scale_filter}[base];"
        f"[1:v]{scale_filter}[ov];"
        f"[base][ov]overlay=0:0:format=auto[outv]"
    )
    cmd = [
        "ffmpeg", "-y", "-i", input_path, "-i", overlay_video,
        "-filter_complex", filter_complex, "-map", "[outv]", "-map", "0:a?",
        "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "copy",
        out_path,
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    shutil.rmtree(tmp_dir, ignore_errors=True)
    print(f"wrote {out_path} ({n_written} frames)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--input", "-i", required=True)
    ap.add_argument("--exercise", "-e", required=True, choices=sorted(EXERCISES.keys()))
    ap.add_argument("--output", "-o", required=True)
    ap.add_argument("--sample-every", type=int, default=2, help="Run pose detection every Nth frame (video only)")
    ap.add_argument("--preview", action="store_true", help="Render at 720p for speed")
    args = ap.parse_args()

    ext = os.path.splitext(args.input)[1].lower()
    if ext in (".jpg", ".jpeg", ".png", ".webp", ".bmp"):
        render_image(args.input, args.exercise, args.output)
    else:
        render_video(args.input, args.exercise, args.output, args.sample_every, args.preview)


if __name__ == "__main__":
    main()
