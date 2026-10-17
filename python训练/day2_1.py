def check_joint_states(joint_states, threshold, velocity_threshold):
    angle_surpass = []
    velocity_surpass = []
    for name, data in joint_states.items():
        angle = data["angle"]
        velocity = data["velocity"]
        if abs(angle) > threshold:
            angle_excess = abs(angle) - threshold
            angle_surpass.append((name, angle, velocity, angle_excess))
        if abs(velocity) > velocity_threshold:
            velocity_excess = abs(velocity) - velocity_threshold
            velocity_surpass.append((name, angle, velocity, velocity_excess))
    return angle_surpass, velocity_surpass


def classify_joint_states(joint_states, threshold, velocity_threshold):
    joint_state = []
    for name, data in joint_states.items():
        angle = data["angle"]
        velocity = data["velocity"]
        angle_abnormal = abs(angle) > threshold
        velocity_abnormal = abs(velocity) > velocity_threshold
        if not angle_abnormal and not velocity_abnormal:
            state = "A"
        elif angle_abnormal and not velocity_abnormal:
            state = "B"
        elif velocity_abnormal and not angle_abnormal:
            state = "C"
        elif angle_abnormal and velocity_abnormal:
            state = "D"
        joint_state.append((name, state))
    return joint_state

joint_states = {
    "shoulder": {"angle": 0.2, "velocity": 0.1},
    "elbow": {"angle": -0.5, "velocity": 0.3},
    "wrist_1": {"angle": 1.1, "velocity": 0.8},
    "wrist_2": {"angle": 0.8, "velocity": 0.4},
    "wrist_3": {"angle": -1.4, "velocity": -0.2},
    "gripper": {"angle": 0.3, "velocity": 0.6}
}

threshold = 1.0
velocity_threshold = 0.7
angle_surpass, velocity_surpass = check_joint_states(joint_states, threshold, velocity_threshold)
for name, angle, velocity, excess in angle_surpass:
    print(f"{name}: angle={angle:.2f}, velocity={velocity:.2f}, excess={excess:.2f}")
for name, angle, velocity, excess in velocity_surpass:
    print(f"{name}: angle={angle:.2f}, velocity={velocity:.2f}, excess={excess:.2f}")
states = classify_joint_states(joint_states, threshold, velocity_threshold)
for name, state in states:
    print(f"{name}: {state}")