# csv -> ndarray -> t-test 

import numpy as np
import csv
import scipy.stats
import pandas as pd


#SOL1 : numpy.genfromtxt()
print('numpy.genfromtxt()')
data1 = np.genfromtxt('CSMHUNT_12300_2022-3-27_4-8-56_0327_30m.csv', delimiter=';', skip_header = 1, dtype = float)
data2 = np.genfromtxt('1CSMHUNT_12300_2022-3-31_3-58-32_100m.csv', delimiter=';', skip_header = 1, dtype = float)
print('data1 and data2')
print(data1)
print('\n')
print(data2)

''' if you wanna get !descriptive mean and std.. : np.average(), np.std()
num1 = data1[:,9]
print('num1 and num2')
print(num1)
avg1 = np.average(num1)
print(avg1)
print('\n')
num2 = data2[:,9]
print(num2)
avg2 = np.average(num2)
print(avg2)
'''

#data1 = data1.tolist()   #trick to get 1XN list
data1 = [i[9] for i in data1]
#data2 = data2.tolist()
data2 = [i[9] for i in data2]
print(len(data1))


'''
#SOL2 : pandas.read_csv()
print('pandas.read_csv()')
df1 = pd.read_csv('CSMHUNT_12300_2022-3-27_4-8-56_0327_30m.csv', sep = ';')
data1 = df1.values
data1 = data1.astype(np.float32)
print(data1)
num1 = data1[:,9]
print(num1)
avg1 = np.average(num1)
print(avg1)

df2 = pd.read_csv('1CSMHUNT_12300_2022-3-31_3-58-32_100m.csv', sep = ';')
data2 = df2.values
data2 = data2.astype(np.float32)
print(data2)
num2 = data2[:,9]
print(num2)
avg2 = np.average(num2)
print(avg2)
'''

#---------t-test-----------------
print("_______t-test______________")
t_result = scipy.stats.ttest_ind(data1,data2,equal_var=False)
print(t_result)
print(">> Meaningful diff if p<0.05")

print("data1") 
print(data1)
