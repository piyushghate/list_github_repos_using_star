import urllib.request 
import json 


# /orgs/:org/repos

# /users/:username/repos

with urllib.request.urlopen("https://api.github.com/orgs/mozilla/repos") as url:
    data = json.loads(url.read().decode())

list1 = []

for each in data:
    if (each['stargazers_count'] != 0):
        stareddata = {
            'name' : each['name'],
            'stars' : each['stargazers_count'],
        }
        list1.append(stareddata)

# print(list1)

newlist = sorted(list1, key=lambda k: k['stars'], reverse=True)

dict1 = { "results" : []}

lengthdict = 0

for each in newlist:
    dict1["results"].append(each)
    lengthdict += 1
    if(lengthdict == 3):
        break

print(json.dumps(dict1))

