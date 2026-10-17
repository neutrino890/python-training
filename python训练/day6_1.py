import json

data = {"thumb": [0.1, 0.19]}

with open("data.json", "w") as f:
    json.dump(data, f)