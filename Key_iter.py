import json
import csv

fileObject = open("./ProductKeys.json", "r")
jsonContent = fileObject.read()
keys = json.loads(jsonContent)
fileObject.close()
lsKeys = [d['ProductKey'] for d in keys]

with open(r'lsIDs_slash.txt', 'w') as fp:
    fp.write('\n'.join(lsKeys))
print("lsIDs_slash.txt written")

# IDkeys with underscore
lsIDs = []
for k in lsKeys:
    sp = k.replace('/','_')
    lsIDs.append(sp)

with open(r'lsIDs_uds.txt', 'w') as fp:
    fp.write('\n'.join(lsIDs))
print("lsIDs_uds.txt written")