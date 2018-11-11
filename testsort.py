import json

list1 = [{'name': 'facebook_business_SDK', 'stars': 2}, {'name': 'list_github_repos_using_star', 'stars': 1}, {'name': 'Weather-app', 'stars': 3}]

# for each in list1:
    # dsorted = sorted(list1, key=list1.get, reverse=True)
newlist = sorted(list1, key=lambda k: k['stars'], reverse=True)
# print(newlist)

dict1 = { "results" : []}

# dict1["result"].append(newlist)

# print(dict1)


for each in newlist:
    dict1["results"].append(each)


print(json.dumps(dict1))

