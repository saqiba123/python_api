import requests

url = "https://www.forbestravelguide.com/award-winners.json?format=json"

payload={}
headers = {
  'Cookie': 'JSESSIONID-FTG=NThhYjE5NTktMWU3NC00OTc5LTgyNjktNTQwODc2MDRlMjM5'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
