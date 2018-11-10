import requests
import json

link = "https://api.github.com/users/piyushghate/repos"
# f = requests.get(link)
# data = json.loads(f.read())
# print(data)

r = requests.get(link)
print(r.json())

# with open('data.json', 'w') as testfile:
#     json.dump(r, testfile)


