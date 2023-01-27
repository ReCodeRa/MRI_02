import json
import pandas as pd

fileObject = open("./ProductKeys.json", "r")
jsonContent = fileObject.read()
keys = json.loads(jsonContent)
fileObject.close()
lsKeys = [d['ProductKey'] for d in keys]

df = pd.DataFrame(lsKeys)
df.to_csv('lsIDs.csv', header=False, index=False)
