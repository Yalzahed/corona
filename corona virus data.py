import urllib.request, json 

with urllib.request.urlopen("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.json") as url:
    data = json.loads(url.read().decode())

json_object = json.dumps(data, indent = 4)

with open('data.json','w') as outfile:
    outfile.write(json_object)








