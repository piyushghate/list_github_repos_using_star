# import requests
# import json

# link = "https://api.github.com/users/piyushghate/repos"
# f = requests.get(link)
# data = json.loads(f.read())
# print(data)

# r = requests.get(link)
# # print(r.json())

# with open('data.json', 'w') as testfile:
#     json.dumps(r)


import urllib.request, json 
with urllib.request.urlopen("https://api.github.com/users/piyushghate/repos") as url:
    data = json.loads(url.read().decode())
    # print(data)

    # with open('data.json', 'w') as testfile:
    #     json.dump(data, testfile)

list1 = []

for each in data:
    if (each['stargazers_count'] != 0):
        # print(each['id'])
        print(each['name'])
        print(each['stargazers_count'])
        stareddata = {
            'name' : each['name'],
            'star' : each['stargazers_count'],
        }
        list1.append(stareddata)

print(list1)
