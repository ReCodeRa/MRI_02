import json
fileObject = open("./ProductKeys.json", "r")
jsonContent = fileObject.read()
keys = json.loads(jsonContent)
fileObject.close()
lsKeys = [d['ProductKey'] for d in keys]
print(lsKeys[0:3])

# Split keys, extract number, save to .csv
lsIDs = []
for k in lsKeys:
    sp = k.split('/')
    print(sp)
    lsIDs.append(sp[2])