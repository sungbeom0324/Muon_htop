# csv -> ndarray -> t-test 

import numpy as np
import csv
import scipy.stats


#py csv.reader + for  
data = []

file = open('1CSMHUNT_12300_2022-3-31_3-58-32_100m.csv', 'r')    # file : file object
reader = csv.reader(file)

for line in reader :
    data.append( line[1: ] )
file.close()

xy = np.array(data[9])  
xy=xy.astype(float)      # float type casting

print(xy)

'''
#np.genfromtxt
data1 = np.genfromtxt('1CSMHUNT_12300_2022-3-31_3-58-32_100m.csv',dtype=None, delimiter=';', names=True)
data2 = np.genfromtxt('2CSMHUNT_12300_2022-4-3_3-45-53_30m.csv',dtype=None, delimiter=';', names=True)
print(type(data1))
print(data1)

print(data1['COINC'])
print(data2['COINC'])
'''

'''
#np.loadtxt
csv_data = np.loadtxt('1CSMHUNT_12300_2022-3-31_3-58-32_100m.csv',delimiter=';')
print(csv_data)
print(type(csv_data))
'''

'''
#---------t-test-----------------
print("t-test")
t_result = scipy.stats.ttest_ind(data1,data2,equal_var=False)
print("t_result")
print(">> Meaningful diff if p<0.05")
'''



