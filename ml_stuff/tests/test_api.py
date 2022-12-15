import json
import requests

url = "http://localhost:8001/score"

data = {"med_inc": 34,
        "house_age": 13,
        "ave_rooms": 7,
        "ave_bdms": 1,
        "pop": 1,
        "ave_occup":752,
        "lat": 2.79,
        "long":39.02
        }

#input_data = np.array([v for k,v in data.dict().items()]).reshape(1,-1)
input_data = json.dumps(data)
headers = {"Content-Type": "application/json"}

resp = requests.post(url, input_data, headers=headers)
print(resp.text)

