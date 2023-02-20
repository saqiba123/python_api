import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"

data ={
    'name': 'Saqiba',
    'roll': 11,
    'city': 'Karachi'

}

#convert the python data (dictionary) into json format:

json_data = json.dumps(data)
#print(type(data))
#we are sending data so uese post method
r = requests.post(url=URL, data= json_data)
#print(r)
data = r.json()
print(data)
