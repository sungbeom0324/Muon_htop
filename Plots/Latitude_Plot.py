#Scattering Plot. Size = coinc / x = latitude , y = altitude
import numpy as np
import matplotlib.pyplot as plt 

alt2 = np.array([19, 36, 59, 67, 60])
lat2 = np.array([33.45, 34.30, 35.14, 35.14, 36.32])
coinc1 = np.array([568.2, 344.4, 378.3, 595.6, 457.4])
coinc2 = np.array([608.6, 632.3, 649.7, 663.3, 671.5])
#coinc_mean1 = np.mean(coinc1)
#coinc_max = np.max(coinc)
#print(coinc_mean)
plt.scatter(lat2, coinc2, color = 'red', alpha = 0.4, s = 500, label = 'Latitude')
plt.legend()

plt.title("Muon counts - Latitude")
plt.savefig("Latitude_Plot.png")

plt.show()


