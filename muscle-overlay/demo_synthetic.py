"""Renders the overlay against fabricated landmarks (no pose detection) so
the capsule geometry can be sanity-checked visually without real footage."""
from PIL import Image, ImageDraw

from render_overlay import build_overlay_frame, roles_for

W, H = 600, 900

# A simple standing figure, arms slightly out, mid-squat.
STANDING_SQUAT = {
    11: (230, 260), 12: (370, 260),   # shoulders
    13: (190, 380), 14: (410, 380),   # elbows
    15: (170, 480), 16: (430, 480),   # wrists
    23: (250, 480), 24: (350, 480),   # hips
    25: (230, 650), 26: (370, 650),   # knees
    27: (240, 800), 28: (360, 800),   # ankles
}


def draw_stick_figure(landmarks):
    img = Image.new("RGB", (W, H), (28, 30, 36))
    draw = ImageDraw.Draw(img)
    bones = [(11, 12), (11, 23), (12, 24), (23, 24), (11, 13), (13, 15),
             (12, 14), (14, 16), (23, 25), (25, 27), (24, 26), (26, 28)]
    for a, b in bones:
        draw.line([landmarks[a], landmarks[b]], fill=(150, 150, 160), width=10)
    for p in landmarks.values():
        r = 8
        draw.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=(200, 200, 210))
    return img


def main():
    for exercise in ["squat", "deadlift", "bench_press", "pull_up", "calf_raise"]:
        base = draw_stick_figure(STANDING_SQUAT).convert("RGBA")
        overlay = build_overlay_frame(W, H, STANDING_SQUAT, roles_for(exercise), t_seconds=0.0)
        out = Image.alpha_composite(base, overlay).convert("RGB")
        path = f"/tmp/claude-0/-home-user-rep-scorer/e87811ee-f96d-543e-9c92-e6a3169bd820/scratchpad/demo_{exercise}.png"
        out.save(path)
        print(path)


if __name__ == "__main__":
    main()
