#correlation calculator

from scipy import stats
import numpy as np

"""
a = np.array([33.45,34.30,35.14,36.32,37.56])
b = np.array([608.6,632.3,663.3,671.5,568.2]) 
"""

a = np.array([30,50,60,74,100,836])
b = np.array([568.2,344.4,378.3,589.9,457.4,535.4,573.3])

print(stats.pearsonr(a,b)) #return : Correlatin Coefficients, p-Value 
