import json
import ast
import pandas as pd

versionFile = open("version.json")
versionData = json.load(versionFile)
#print(type(versionData))

#astifiedVersionData = ast.literal_eval(versionData)
#print(astifiedVersionData)

#parsedVersionData = json.loads(json.dumps(astifiedVersionData))
#print(parsedVersionData)

decodedVersionData = json.loads(json.dumps(versionData))
for key in decodedVersionData:
    dict(decodedVersionData).get(key).pop("distributionCounter")
#dict(decodedVersionData).get("").pop("distributionCounter")

#pd.json_normalize(versionData, record_path=[''], meta=[''], meta_prefix='-', record_prefix='-')
pd.set_option('display.max_columns', None)
df = pd.DataFrame.from_dict(decodedVersionData,orient='index')
#print(decodedVersionData)
versionInText = df
#print(df)
versionInTextFile = open("versionInTextFile","w")
versionInTextFile.write(str(versionInText))
versionInTextFile.close()
