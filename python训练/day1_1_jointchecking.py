joint_angles = [0.2, -0.5, 1.1, 0.8, -1.4, 0.3]
joint_count = len(joint_angles)
extreme_joint_count = 0
for i, angle in enumerate(joint_angles, start=1):
    if abs(angle) > 1.0:
        print(f"Joint {i} is out of range: {angle}")
        extreme_joint_count += 1
    else:
        print(f"Joint {i} is within range: {angle}")
print(f"Total joints: {joint_count}")
print(f"Extreme joints: {extreme_joint_count}")