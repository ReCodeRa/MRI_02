import json
fileObject = open("./MRI/ProductKeys.json", "r")
jsonContent = fileObject.read()
keys = json.loads(jsonContent)
print(type(keys))
# print(keys)
lsKeys = [d.values() for d in keys]

# lsKeys = []
# for i in keys:
#     print(i.values())
#     # lsKeys.append(i.values())
print(lsKeys[0:3])