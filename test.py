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


for each in data:
    if (each['stargazers_count'] == 1):
        print(each['id'])