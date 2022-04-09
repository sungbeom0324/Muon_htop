#Scattering Plot. Size = coinc / x = latitude , y = altitude
import numpy as np
import matplotlib.pyplot as plt 

alt1 = np.array([30.0, 50, 60, 74, 100,836])
alt2 = np.array([19, 36, 59, 67, 60])
lat1 = np.array([37.56, 37.56, 37.56, 37.56, 37.56, 37.66])
lat2 = np.array([33.45, 34.30, 35.14, 35.14, 36.32])
coinc1 = np.array([568.2, 344.4, 378.3, 595.6, 457.4, 522.1])
coinc2 = np.array([608.6, 632.3, 649.7, 663.3, 671.5])
#coinc_mean1 = np.mean(coinc1)
#coinc_max = np.max(coinc)
#print(coinc_mean)
plt.scatter(lat1, alt1, color = 'red', alpha = 0.4, s = coinc1, label = 'Altitude')
plt.scatter(lat2, alt2, color = 'blue', alpha = 0.4, s = coinc2, label = 'Latitude')
plt.legend()

plt.title("Size of Dot = Relative Muon Counts")
plt.savefig("BrokenAxis_Muon_Location_ScatteringPlot.png")

plt.show()


