import urllib.request 
import json 




# inputfromuser = input("Please mention the org name: ")
def run_api(input_json):
    
    json_string = json.dumps(input_json)

    return json_string

    # inputobj = {
    #     'org' : inputfromuser, 
    # }

    # inputjson = json.dumps(inputobj)
    # print("Input given as: ",inputjson)

    # inputlist1 = []

    # inputlist1.append(inputobj)

    # orgname = inputlist1[0]["org"]

    # # /orgs/:org/repos

    # # /users/:username/repos

    # url1 = "https://api.github.com/orgs/" +orgname+"/repos"

    # with urllib.request.urlopen(url1) as url:
    #     data = json.loads(url.read().decode())

    # list1 = []

    # for each in data:
    #     if (each['stargazers_count'] != 0):
    #         stareddata = {
    #             'name' : each['name'],
    #             'stars' : each['stargazers_count'],
    #         }
    #         list1.append(stareddata)

    # newlist = sorted(list1, key=lambda k: k['stars'], reverse=True)

    # dict1 = { "results" : []}

    # lengthdict = 0

    # for each in newlist:
    #     dict1["results"].append(each)
    #     lengthdict += 1
    #     if(lengthdict == 3):
    #         break

    # print(json.dumps(dict1))

