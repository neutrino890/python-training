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

abnormal_counts = []
abnormal_joint_lists = []

for frame in frames:
    count = 0
    abnormal_joints = []
    for joint, position in frame.items():
        if position != "A":
            count += 1
            abnormal_joints.append(joint)
    abnormal_counts.append(count)
    abnormal_joint_lists.append(abnormal_joints)

print(abnormal_counts)
print("Abnormal joints in each frame:")
print(abnormal_joint_lists)
