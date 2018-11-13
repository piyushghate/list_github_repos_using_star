import urllib.request 
import json 

#To open and read the url:
with urllib.request.urlopen("https://api.github.com/users/piyushghate/repos") as url:   
    data = json.loads(url.read())

#empty list to hold the repo data with stargazers_count
list1 = []

for each in data:
    if (each['stargazers_count'] != 0):         # any repo with stargazers_count greater than 0 appended in list1
        stareddata = {
            'name' : each['name'],
            'stars' : each['stargazers_count'],
        }
        list1.append(stareddata)

print(list1)