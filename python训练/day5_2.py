frames = (
    {"thumb": "A", "index": "B"},
    {"thumb": "B", "index": "B"},
    {"thumb": "B", "index": "A"},
    {"thumb": "A", "index": "D"},
)

start_frames = {
    "thumb": None,
    "index": None,
}

segments = {
    "thumb": [],
    "index": [],
}

for i, frame in enumerate(frames):
    for joint, state in frame.items():
        if state != "A" and start_frames[joint] is None:
            start_frames[joint] = i
        if state == "A" and start_frames[joint] is not None:
            segments[joint].append((start_frames[joint], i-1))
            start_frames[joint] = None

for joint in start_frames:
    if start_frames[joint] is not None:
        segments[joint].append(
            (start_frames[joint], len(frames) - 1)
        )

print(start_frames)
print(segments)
