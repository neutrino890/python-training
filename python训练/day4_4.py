frames = (
    {"thumb": "B", "index": "A", "middle": "A"},
    {"thumb": "B", "index": "B", "middle": "A"},
    {"thumb": "D", "index": "B", "middle": "A"},
    {"thumb": "A", "index": "B", "middle": "B"},
    {"thumb": "B", "index": "A", "middle": "B"},
    {"thumb": "B", "index": "B", "middle": "A"},
)

def analyze_max_consecutive_abnormal(frames):
    if not frames:
        return {}


    current_counts = {joint: 0 for joint in frames[0].keys()}

    max_counts = {joint: 0 for joint in frames[0].keys()}

    for frame in frames:
        for joint, position in frame.items():
            if position != "A":
                current_counts[joint] += 1
                max_counts[joint] = max(max_counts[joint], current_counts[joint])
            else:
                current_counts[joint] = 0
        
    return max_counts

result = analyze_max_consecutive_abnormal(frames)
print("thumb max abnormal", result["thumb"])
print("index max abnormal", result["index"])
print("middle max abnormal", result["middle"])

print(analyze_max_consecutive_abnormal(()))
