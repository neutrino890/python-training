frames = (
    {
        "shoulder": "A",
        "elbow": "A",
        "wrist_1": "B",
    },

    {
        "shoulder": "A",
        "elbow": "D",
        "wrist_1": "A",
    },

    {
        "shoulder": "B",
        "elbow": "A",
        "wrist_1": "D",
    }
)

def analyze_frames(frames):
    abnormal_counts = []
    abnormal_joints_list = []

    for frame in frames:
        count = 0
        abnormal_joints = []
        for joint, position in frame.items():
            if position != "A":
                count += 1
                abnormal_joints.append(joint)
        abnormal_joints_list.append(abnormal_joints)
        abnormal_counts.append(count)

    return abnormal_counts, abnormal_joints_list

abnormal_counts, abnormal_joints_list = analyze_frames(frames)
print("Total abnormal counts:", abnormal_counts)
print("Abnormal joints:", abnormal_joints_list)
print(analyze_frames(()))