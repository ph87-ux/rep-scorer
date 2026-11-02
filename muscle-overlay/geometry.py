"""Turns pose landmarks + a muscle-region spec into a drawable capsule."""
import math

MIRROR = {11: 12, 12: 11, 13: 14, 14: 13, 15: 16, 16: 15, 23: 24, 24: 23, 25: 26, 26: 25, 27: 28, 28: 27}


def _mirror(idx):
    return MIRROR.get(idx, idx)


def region_capsule(landmarks, spec, side, torso_scale):
    """landmarks: dict[int -> (x, y)] in pixel space.
    Returns (rect_points[4], (cx1, cy1, r1), (cx2, cy2, r2)) or None if landmarks missing.
    """
    j1, j2 = spec["joints"]
    if spec.get("midline"):
        if not all(k in landmarks for k in (11, 12, 23, 24)):
            return None
        p1 = _mid(landmarks[11], landmarks[12])
        p2 = _mid(landmarks[23], landmarks[24])
    else:
        if side == "R":
            j1, j2 = _mirror(j1), _mirror(j2)
        if j1 not in landmarks or j2 not in landmarks:
            return None
        p1, p2 = landmarks[j1], landmarks[j2]

    offset = spec["offset"]
    if side == "R" and not spec.get("midline"):
        offset = -offset

    if spec.get("is_point"):
        r = spec["width"] * torso_scale
        cx, cy = p1
        return None, (cx, cy, r), None

    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    length = math.hypot(dx, dy)
    if length < 1e-6:
        return None
    ux, uy = dx / length, dy / length
    perp = (-uy, ux)

    clip = spec.get("clip", 0.0)
    p1c = (p1[0] + ux * length * clip, p1[1] + uy * length * clip)
    p2c = (p2[0] - ux * length * (clip * 0.3), p2[1] - uy * length * (clip * 0.3))

    off = (perp[0] * offset * length, perp[1] * offset * length)
    c1 = (p1c[0] + off[0], p1c[1] + off[1])
    c2 = (p2c[0] + off[0], p2c[1] + off[1])

    half_w = spec["width"] * length / 2
    side_vec = (perp[0] * half_w, perp[1] * half_w)
    rect = [
        (c1[0] + side_vec[0], c1[1] + side_vec[1]),
        (c2[0] + side_vec[0], c2[1] + side_vec[1]),
        (c2[0] - side_vec[0], c2[1] - side_vec[1]),
        (c1[0] - side_vec[0], c1[1] - side_vec[1]),
    ]
    return rect, (c1[0], c1[1], half_w), (c2[0], c2[1], half_w)


def _mid(a, b):
    return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)


def torso_scale(landmarks):
    if 11 in landmarks and 23 in landmarks:
        return math.hypot(landmarks[11][0] - landmarks[23][0], landmarks[11][1] - landmarks[23][1])
    return 100.0
