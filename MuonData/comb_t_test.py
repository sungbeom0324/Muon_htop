#combinaton of files in directory -> t-test

import os #os.listdir()
import itertools #itertools.combinations()
import numpy as np #numpy.genfromtxt()
import scipy.stats #stats.ttest_ind()

path = "./"
file_list = os.listdir(path)
file_list = [s for s in file_list if 'CSMHUNT' in s]
print('file_list')
print(file_list)

for comb in itertools.combinations(file_list, 2):
    data0 = np.genfromtxt(comb[0], delimiter=';', skip_header=1, dtype=float)
    data1 = np.genfromtxt(comb[1], delimiter=';', skip_header=1, dtype=float)
    data0 = [i[9] for i in data0]
    data1 = [j[9] for j in data1] 
    #print(data0)
    #print(data1)    
    tag0 = comb[0].split('_')
    tag0 = tag0[-1]
    tag1 = comb[1].split('_')
    tag1 = tag1[-1]
           
    #t-test
    #print("_______t-test______________")
    t_result = scipy.stats.ttest_ind(data0,data1,equal_var=False)
    if t_result[1] > 0.05 :    
        print("_______t-test______________")
        print("%s vs %s" %(tag0,tag1))
        print(t_result) 
        #print(">> Meaningful diff if p<0.05")
