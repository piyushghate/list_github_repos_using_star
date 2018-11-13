import json

inputfromuser = input("Please mention the org name: ")      #org name from user used directly in the url below

url1 = "https://api.github.com/orgs/" +inputfromuser+"/repos"
print(url1)