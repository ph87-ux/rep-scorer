"""Muscle region geometry (anchored to MediaPipe Pose landmarks) and
exercise -> muscle-role mappings."""

# MediaPipe Pose landmark indices we use.
L_SHOULDER, R_SHOULDER = 11, 12
L_ELBOW, R_ELBOW = 13, 14
L_WRIST, R_WRIST = 15, 16
L_HIP, R_HIP = 23, 24
L_KNEE, R_KNEE = 25, 26
L_ANKLE, R_ANKLE = 27, 28

# Each region is drawn as a capsule (thick rounded line) between two
# landmarks, offset perpendicular to the limb by `offset` (fraction of the
# segment length, signed: positive = one side, negative = the other) and
# thickened by `width` (fraction of segment length). `sides` lists which
# body sides ('L', 'R') the region applies to; a region with a single side
# entry of None spans the torso and isn't mirrored.
MUSCLE_REGIONS = {
    "chest":     {"joints": (L_SHOULDER, R_SHOULDER), "offset": -0.55, "width": 0.55, "sides": [None]},
    "shoulders": {"joints": (L_SHOULDER, L_SHOULDER), "offset": 0.0, "width": 0.16, "sides": ["L", "R"], "is_point": True},
    "biceps":    {"joints": (L_SHOULDER, L_ELBOW), "offset": 0.28, "width": 0.5, "sides": ["L", "R"]},
    "triceps":   {"joints": (L_SHOULDER, L_ELBOW), "offset": -0.28, "width": 0.45, "sides": ["L", "R"]},
    "forearms":  {"joints": (L_ELBOW, L_WRIST), "offset": 0.0, "width": 0.4, "sides": ["L", "R"]},
    "abs":       {"joints": (L_SHOULDER, L_HIP), "offset": 0.0, "width": 0.55, "sides": [None], "midline": True},
    "lats":      {"joints": (L_SHOULDER, L_HIP), "offset": 0.35, "width": 0.55, "sides": ["L", "R"]},
    "glutes":    {"joints": (L_HIP, L_KNEE), "offset": -0.3, "width": 0.6, "sides": ["L", "R"], "clip": 0.32},
    "quads":     {"joints": (L_HIP, L_KNEE), "offset": 0.3, "width": 0.55, "sides": ["L", "R"]},
    "hamstrings":{"joints": (L_HIP, L_KNEE), "offset": -0.3, "width": 0.5, "sides": ["L", "R"]},
    "calves":    {"joints": (L_KNEE, L_ANKLE), "offset": -0.3, "width": 0.55, "sides": ["L", "R"]},
}

MUSCLE_COLORS = {
    "chest": (255, 90, 70), "shoulders": (255, 150, 60), "biceps": (255, 196, 60),
    "triceps": (255, 150, 150), "forearms": (255, 214, 120), "abs": (120, 220, 255),
    "lats": (150, 130, 255), "glutes": (255, 90, 180), "quads": (169, 225, 84),
    "hamstrings": (100, 200, 140), "calves": (90, 200, 255),
}

EXERCISES = {
    "squat": {"primary": ["quads", "glutes"], "secondary": ["hamstrings", "calves", "abs"]},
    "front_squat": {"primary": ["quads"], "secondary": ["glutes", "abs"]},
    "deadlift": {"primary": ["glutes", "hamstrings"], "secondary": ["lats", "forearms", "abs"]},
    "romanian_deadlift": {"primary": ["hamstrings", "glutes"], "secondary": ["lats", "forearms"]},
    "bench_press": {"primary": ["chest", "triceps"], "secondary": ["shoulders"]},
    "overhead_press": {"primary": ["shoulders", "triceps"], "secondary": ["abs"]},
    "pull_up": {"primary": ["lats", "biceps"], "secondary": ["forearms", "shoulders"]},
    "lat_pulldown": {"primary": ["lats", "biceps"], "secondary": ["forearms"]},
    "push_up": {"primary": ["chest", "triceps"], "secondary": ["shoulders", "abs"]},
    "row": {"primary": ["lats", "biceps"], "secondary": ["shoulders", "forearms"]},
    "bicep_curl": {"primary": ["biceps"], "secondary": ["forearms"]},
    "tricep_extension": {"primary": ["triceps"], "secondary": ["forearms"]},
    "lunge": {"primary": ["quads", "glutes"], "secondary": ["hamstrings", "calves"]},
    "hip_thrust": {"primary": ["glutes"], "secondary": ["hamstrings", "abs"]},
    "plank": {"primary": ["abs"], "secondary": ["shoulders"]},
    "calf_raise": {"primary": ["calves"], "secondary": []},
}
