import urllib.request 
import json 


def run_api(jsonformat):
    
    json_string = json.dumps(jsonformat)

    inputobj = json.loads(json_string)

    print("Input given as: ",json_string)

    inputlist1 = []

    inputlist1.append(inputobj)

    orgname = inputlist1[0]["org"]

        # /orgs/:org/repos

        # /users/:username/repos

    url1 = "https://api.github.com/orgs/" +orgname+"/repos"

    with urllib.request.urlopen(url1) as url:
            data = json.loads(url.read().decode())

    list1 = []

    for each in data:
        if (each['stargazers_count'] != 0):
            stareddata = {
                'name' : each['name'],
                'stars' : each['stargazers_count'],
            }
            list1.append(stareddata)

    newlist = sorted(list1, key=lambda k: k['stars'], reverse=True)

    finallist = []
    lengthdict = 0

    for each in newlist:
        finallist.append(each)
        lengthdict += 1
        if(lengthdict == 3):
            break

    return json.dumps(finallist)

