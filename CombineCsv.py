# combining csv

import pandas as pd
import glob
import os

input_file = r"/home/stiger97/muon2022"
output_file = r"/home/stiger97/muon2022/Hyeoksin2day.csv"

allFile_list = glob.glob(os.path.join(input_file, '*Hyeoksin*.csv'))
print(allFile_list)
allData = []
for file in allFile_list:
    df = pd.read_csv(file)
    allData.append(df) 

dataCombine = pd.concat(allData, axis=0, ignore_index=True) 

dataCombine.to_csv(output_file, index=True)  #True -> index in order.  



