frames = (
    {"thumb": "B", "index": "A", "middle": "A"},
    {"thumb": "B", "index": "B", "middle": "A"},
    {"thumb": "D", "index": "B", "middle": "A"},
    {"thumb": "A", "index": "B", "middle": "B"},
    {"thumb": "B", "index": "A", "middle": "B"},
    {"thumb": "B", "index": "B", "middle": "A"},
)

current_counts = {
    "thumb": 0,
    "index": 0,
    "middle": 0,
}

max_counts = {
    "thumb": 0,
    "index": 0,
    "middle": 0,
}

for frame in frames:
    for joint, position in frame.items():
        if position != "A":
            current_counts[joint] += 1
            max_counts[joint] = max(max_counts[joint], current_counts[joint])
        else:
            current_counts[joint] = 0


print("thumb max abnormal", max_counts["thumb"])
print("index max abnormal", max_counts["index"])
print("middle max abnormal", max_counts["middle"])


