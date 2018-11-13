import json

list1 = [{'name': 'facebook_business_SDK', 'stars': 2}, {'name': 'list_github_repos_using_star', 'stars': 1}, {'name': 'Weather-app', 'stars': 3}]

print(sorted(list1, key=lambda k: k['stars'], reverse=True))        # sorting and priting in decending order