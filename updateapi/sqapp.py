import requests
import json

URL = "http://127.0.0.1:8000/sturetrive/"
# this third party app need data from website/stored data

# meke request


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)

    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)

# fro reading the data from db
# get_data(2)


def post_data():
    data = {
        'name': 'hira',
        'roll': 200,
        'school': 'NED'
    }
    # convert python dictionary into json format
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)


#post_data()

def update_data():
    data = {
        'id': 4,
        'name': 'heer',
        'roll': 250,
        'school': 'IICT'
    }
    # convert python dictionary into json format
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)


#update_data()

def delete_data():
    data = {
        'id': 4
    }
    # convert python dictionary into json format
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)


delete_data()