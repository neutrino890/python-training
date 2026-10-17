def find_abnormal_segments(frames):
    if not frames:
        return {}
    
    start_frames = {
        joint: None for joint in frames[0].keys()
    }

    segments = {
        joint: [] for joint in frames[0].keys()
    }

    for i, frame in enumerate(frames):
        for joint, state in frame.items():
            if state in ("B", "D") and start_frames[joint] is None:
                start_frames[joint] = i
            elif state == "A" and start_frames[joint] is not None:
                segments[joint].append((start_frames[joint], i-1))
                start_frames[joint] = None
            elif state is None:
                if start_frames[joint] is not None:
                    segments[joint].append(
                        (start_frames[joint], i - 1)
                    )
                    start_frames[joint] = None


    for joint in start_frames:
        if start_frames[joint] is not None:
            segments[joint].append(
                (start_frames[joint], len(frames) - 1)
            )

    return segments

frames = (
    {"thumb": "B", "index": "A"},  # 第 0 帧
    {"thumb": None, "index": "D"}, # 第 1 帧
    {"thumb": "B", "index": "D"},  # 第 2 帧
    {"thumb": "A", "index": None}, # 第 3 帧
)
print(find_abnormal_segments(frames))