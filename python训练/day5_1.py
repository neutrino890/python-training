states = ("B", "D", "B")
abnormal_segments = []
start_frame = None
for i, state in enumerate(states):
    if state != "A":
        if start_frame is None:
            start_frame = i
    else:
        if start_frame is not None:
            abnormal_segments.append((start_frame, i - 1))
            start_frame = None

if start_frame is not None:
    abnormal_segments.append((start_frame, len(states) - 1))


print(abnormal_segments)