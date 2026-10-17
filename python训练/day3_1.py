states = {
    "shoulder": "A",
    "elbow": "D",
    "wrist_1": "B",
    "wrist_2": "A",
    "wrist_3": "C",
    "gripper": "D"
}

def check_joint_states(states):
    count_A = 0
    count_B = 0
    count_C = 0
    count_D = 0
    abnormal_count = 0
    for state in states.values():
        if state == "A":
            count_A += 1
        elif state == "B":
            count_B += 1
            abnormal_count+= 1
        elif state == "C":
            count_C += 1
            abnormal_count += 1
        elif state == "D":
            count_D += 1
            abnormal_count += 1
    return count_A, count_B, count_C, count_D, abnormal_count

count_A, count_B, count_C, count_D, abnormal_count = check_joint_states(states)
print(f"Count of A: {count_A}")
print(f"Count of B: {count_B}")
print(f"Count of C: {count_C}")
print(f"Count of D: {count_D}")
print(f"abnormal_count: {abnormal_count}")