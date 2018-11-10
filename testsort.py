list1 = [{'name': 'facebook_business_SDK', 'star': 2}, {'name': 'list_github_repos_using_star', 'star': 1}, {'name': 'Weather-app', 'star': 3}]

# for each in list1:
    # dsorted = sorted(list1, key=list1.get, reverse=True)
newlist = sorted(list1, key=lambda k: k['star'], reverse=True)
print(newlist)