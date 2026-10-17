def check_joints(joint_angles, threshold):
    if not joint_angles:
        return 0, [], [], []
    extreme_joint_count = 0
    indices = []
    extreme_angles = []
    excess = []
    for i, angle in enumerate(joint_angles, start=0):
        if abs(angle) > threshold:
            extreme_joint_count += 1
            indices.append(i)
            surpass = abs(angle) - threshold
            extreme_angles.append(angle)
            excess.append(surpass)
        else:
            continue
    return extreme_joint_count, indices, extreme_angles, excess


count, indices, extreme_angles, excess = check_joints(
    [0.2, -0.5, 1.1, 0.8, -1.4, 0.3],
    1.0
)
for i, angle, surpass in zip(indices, extreme_angles, excess):
    print(f"extreme joint: {i}, angle: {angle}, surpass: {surpass}")
print(count)
print(indices)
print(extreme_angles)
print(excess)