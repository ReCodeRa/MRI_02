import json
fileObject = open("./MRI/ProductKeys.json", "r")
jsonContent = fileObject.read()
keys = json.loads(jsonContent)
print(type(keys))
# print(keys)
lsKeys = [d['ProductKey'] for d in keys]
print(lsKeys[0:3])