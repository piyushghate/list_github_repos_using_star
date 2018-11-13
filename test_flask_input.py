import requests
import json

# making a post request @http://127.0.0.1:5000/repos with header as ({'Content-Type': 'application/json'}) and data as ({'org': 'google'})
r = requests.post('http://127.0.0.1:5000/repos', data=json.dumps({'org': 'google'}), headers={'Content-Type': 'application/json'})

print(r)
print(r.headers)
print(r.content)