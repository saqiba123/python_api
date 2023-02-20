import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"

data ={
    'name':'bushra',
    'roll': 102,
    'city': 'bhitshah'
}

#convert python obj into json

json_data = json.dumps(data) 

r = requests.post(url= URL, data= json_data)

data = r.json()

print(data)