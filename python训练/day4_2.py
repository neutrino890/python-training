states = ("B", "B", "D", "A", "B", "A", "B", "B")

current_count = 0
max_count = 0

for state in states:
    if state != "A":
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        current_count = 0

print("Maximum consecutive abnormal states:", max_count)