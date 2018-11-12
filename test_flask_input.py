import requests
import json

url = 'http://127.0.0.1:5000/'
headers = {'Content-Type': 'application/json'}
data = {'email' : 'piyushghate17@gmail.com', 'name' : 'Piyush', 'angel_list' : 'https://angel.co/piyush-ghate', 'github' : 'https://github.com/piyushghate'}

r = requests.post(url,data=json.dumps(data), headers=headers)

print(r)
print(r.headers)
print(r.content)