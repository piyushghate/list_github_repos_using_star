import requests
import json

# making a post request @http://127.0.0.1:5000/repos with header as ({'Content-Type': 'application/json'}) and data as ({'org': 'google'})
r = requests.post('http://127.0.0.1:5000/repos', data=json.dumps({'org': 'google'}), headers={'Content-Type': 'application/json'})

print(r)            # to check the status code 
print(r.headers)    # to print the header info
print(r.content)    # to print the data provided by the server