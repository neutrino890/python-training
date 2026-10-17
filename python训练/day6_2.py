import json

def frame_to_time(frame_index, sample_rate):
    return frame_index / sample_rate

def segment_to_time(start_frame, end_frame, sample_rate):
    start_time = frame_to_time(start_frame, sample_rate)
    end_time = frame_to_time(end_frame, sample_rate)
    duration = end_time - start_time
    return start_time, end_time, duration

segments = {
    "thumb": [(10, 19), (35, 39)],
    "index": [(20, 24)]
}
sample_rate = 100

time_segments = {joint: [] for joint in segments}
for joint, joint_segments in segments.items():
    
    for start_frame, end_frame in joint_segments:
        start_time, end_time, duration = segment_to_time(start_frame, end_frame, sample_rate)
        segment_info = {
            "start_time": start_time,
            "end_time": end_time,
            "duration": duration,
        }
        time_segments[joint].append(segment_info)
        print(joint, start_time, end_time, duration)

with open("time_segments.json", "w") as f:
    json.dump(time_segments, f)

with open("time_segments.json", "r") as f:
    loaded_data = json.load(f)

print(loaded_data)