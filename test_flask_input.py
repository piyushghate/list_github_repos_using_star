import requests
import json

url = 'http://127.0.0.1:5000/repo'
headers = {'Content-Type': 'application/json'}
data = {'org': 'mozilla'}

r = requests.post(url,data=json.dumps(data), headers=headers)

print(r)
print(r.headers)
print(r.content)