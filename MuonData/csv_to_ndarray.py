import numpy as np
import io #io.open -> debugs encoding error
#-------------------------
#SOL1 : numpy.genfromtxt()
print('numpy.genfromtxt()')
data = np.genfromtxt('CSMHUNT_12300_2022-3-27_4-8-56_0327_30m.csv', delimiter=';', skip_header = 1, dtype = float)
print(data)

num = data[:,9]
print(num)
avg = np.average(num)
print(avg)

#-------------------------
#SOL2 : pandas.read_csv()
print('pandas.read_csv()')
import pandas as pd
df = pd.read_csv('CSMHUNT_12300_2022-3-27_4-8-56_0327_30m.csv', sep = ';')
data = df.values
print(data)

num = data[:,9]
print(num)
avg = np.average(num)
print(avg)

#-------------------------
#SOL3 : python standard library, csv.reader.
print('csv.reader')
import csv
with io.open('CSMHUNT_12300_2022-3-27_4-8-56_0327_30m.csv', 'r', encoding='utf8') as f : 
    dat = [k for k in csv.reader(f)] 

'''
#-------------------------
#SOL4 : numpy.loadtxt()
data = np.loadtxt('CSMHUNT_12300_2022-3-27_4-8-56_0327_30m.csv', delimiter = ';', skiprows=1) #dtype = float is difault but !ABC
muon = data[:,9]
'''

#-------------------------
#SOL5 : python basic function : open & for
print('open & for')
data = io.open('CSMHUNT_12300_2022-3-27_4-8-56_0327_30m.csv', 'r', encoding = 'utf-8')
print(data)

