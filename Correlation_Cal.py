#correlation calculator

from scipy import stats
import numpy as np

a = np.array([33.45,34.30,35.14,36.32,37.56])
b = np.array([608.6,632.3,663.3,671.5,568.2]) 

print(stats.pearsonr(a,b)) #return : Correlatin Coefficients, p-Value 
