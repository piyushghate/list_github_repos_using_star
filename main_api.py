import urllib.request 
import json 


def run_api(jsonformat):    # function which is called in flask_main file
    
    # fetching org name from data passed to run_api function
    print("org ID: ", jsonformat['org'])

    #To open and read the url:
    with urllib.request.urlopen("https://api.github.com/orgs/" +jsonformat['org']+"/repos") as url:
            data = json.loads(url.read())

    #empty list to hold the repo data with stargazers_count
    list1 = []

    for each in data:
        if (each['stargazers_count'] != 0):         # get all the repos with non zero stars
            stareddata = {                          # obj which will hold name and stars of the repo
                'name' : each['name'],
                'stars' : each['stargazers_count'],
            }
            list1.append(stareddata)

    newlist = sorted(list1, key=lambda k: k['stars'], reverse=True)     # this will sort the list for repos in decending order for stars

    finallist = []      #final list to hold the first three repos

    lengthdict = 0      

    for each in newlist:
        finallist.append(each)
        if(lengthdict == 2):    # allows only 0, 1 and 2nd position elements from newlist into finallist
            break
        lengthdict += 1

    return finallist    # finally passing the list holding 3 repos with maximum stars

