import json
filename="f:\Testjson.json"
a=[1,2,3,4]
with open(filename,'w') as file:
    json.dumps(a,file)
    