"""Pose landmark extraction for a still image or every frame of a video."""
import cv2
import mediapipe as mp

_POSE_LANDMARKS = list(range(33))


def _to_pixel_landmarks(result, w, h, min_visibility=0.4):
    if not result.pose_landmarks:
        return None
    out = {}
    for i, lm in enumerate(result.pose_landmarks.landmark):
        if lm.visibility >= min_visibility:
            out[i] = (lm.x * w, lm.y * h)
    return out or None


def extract_image(path):
    mp_pose = mp.solutions.pose
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(path)
    h, w = img.shape[:2]
    with mp_pose.Pose(static_image_mode=True, model_complexity=2) as pose:
        result = pose.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    return w, h, _to_pixel_landmarks(result, w, h)


def extract_video(path, sample_every=1):
    """Yields (frame_index, landmarks_or_None). Runs pose on every
    `sample_every`-th frame; frames in between reuse the last detection."""
    mp_pose = mp.solutions.pose
    cap = cv2.VideoCapture(path)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    last = None
    with mp_pose.Pose(static_image_mode=False, model_complexity=1) as pose:
        i = 0
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            if i % sample_every == 0:
                result = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                last = _to_pixel_landmarks(result, w, h) or last
            yield i, last
            i += 1
    cap.release()
    extract_video.meta = {"width": w, "height": h, "fps": fps, "n_frames": n_frames}
