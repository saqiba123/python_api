#seperate application in python wants to communicate with DRF () rest api
import requests
URL = "http://127.0.0.1:8000/Studentinfo/"

r = requests.get(url=URL)

data = r.json()
print(data)