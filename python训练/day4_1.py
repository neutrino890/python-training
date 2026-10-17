frames = (
    {"shoulder": "A", "elbow": "B", "wrist": "A"},
    {"shoulder": "A", "elbow": "B", "wrist": "A"},
    {"shoulder": "A", "elbow": "D", "wrist": "A"},
    {"shoulder": "A", "elbow": "A", "wrist": "B"},
    {"shoulder": "A", "elbow": "A", "wrist": "B"},
)
abnormal_counts = {
    "shoulder": 0,
    "elbow": 0,
    "wrist": 0
}

for frame in frames:
    for joint, position in frame.items():
        if position != "A":
            abnormal_counts[joint] += 1

print("Abnormal shoulder count:", abnormal_counts["shoulder"])
print("Abnormal elbow count:", abnormal_counts["elbow"])
print("Abnormal wrist count:", abnormal_counts["wrist"])