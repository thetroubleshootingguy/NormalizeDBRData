import json
import ast

import numpy as np
import pandas as pd

from matplotlib import pyplot as plt

#dbrReceiver = open("dbr-reciever.json")
#dbrReceiverData = json.load(dbrReceiver)

#decodedDbrReceiverData = json.loads(json.dumps(dbrReceiverData))

#for key in decodedDbrReceiverData:
    #print(key)
    #print(key + " : " + str(decodedDbrReceiverData.get(key)))

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
#df = pd.DataFrame.from_dict(decodedDbrReceiverData,orient='index')
#print(df)
decodedDbrReceiverData = pd.read_json("dbr-reciever.json")
level1DF = pd.DataFrame(decodedDbrReceiverData)
level1DF.replace(np.nan,0, inplace=True)
dbrReceiver = open("dbrReceiver.txt","w")
level1DFT = level1DF.head().transpose()
dbrReceiver.write(str(level1DFT))
dbrReceiver.close()

level1DFT.plot.bar()
plt.show()
