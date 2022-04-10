###correlation calculator#######

from scipy import stats
import numpy as np
import scipy.stats

print("-------------------------------------------")
print("Relative Coefficient, p-value")

# Latitude
l = np.array([33.45,34.30,35.14,36.32,37.56])
c1 = np.array([608.6,632.3,663.3,671.5,568.2]) 
print("Latitude")
print(stats.pearsonr(l,c1)) #return : Correlatin Coefficients, p-Value 

# Altitude
a = np.array([30,50,60,74,100,836])
c2 = np.array([568.2,344.4,378.3,589.9,457.4,535.4])
print("Altitude")
print(stats.pearsonr(a,c2)) #return : Correlatin Coefficients, p-Value 

print("-------------------------------------------")

###t-test############################
print("t_test")
lat_mean = np.mean(c1)
alt_maen = np.mean(c2)
t_result = scipy.stats.ttest_ind(c1,c2,equal_var=False) 
print(t_result)
print(">>Meaningful difference btw lat, alt means")
