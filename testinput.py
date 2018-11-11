import json


inputfromuser = input("Please mention the org name: ")

inputobj = {
    'org' : inputfromuser, 
}

inputjson = json.dumps(inputobj)
print("Input given as: ",inputjson)

# print(type(inputjson))
print("InputJSON:", inputjson)




# jsonstring = {"org" : "mozilla"}
# print(type(jsonstring))



# print("jsonstring",json.dumps(jsonstring))

inputlist1 = []

inputlist1.append(inputobj)
print(inputlist1)

orgname = inputlist1[0]["org"]
# print(orgname)

url1 = "https://api.github.com/orgs/" +orgname+"/repos"
print(url1)