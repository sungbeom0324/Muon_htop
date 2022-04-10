# combination of files in a directory.
# 4 space bar!

import os

#SOL1 : os.listdir()
path = "./"
file_list = os.listdir(path)
file_list = [s for s in file_list if 'CSMHUNT' in s]
print(file_list)

for file1 in file_list:     #OPTIONAL : designate tag name
    tag1 = file1.split('_')
    tag1 = tag1[-1] 

import itertools #Combination : itertools.combinations() 
for comb in itertools.combinations(file_list, 2):
    print(comb[1])
    
  
