import json

with open('hub\data.json') as f:
    data = json.load(f)

print(data["events_data"][0]['id'])