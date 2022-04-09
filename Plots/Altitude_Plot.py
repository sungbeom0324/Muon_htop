#Scattering Plot. Size = coinc / x = latitude , y = altitude
import numpy as np
import matplotlib.pyplot as plt 

alt1 = np.array([30.0, 50, 60, 74, 100])
lat1 = np.array([37.56, 37.56, 37.56, 37.56, 37.56])
coinc1 = np.array([568.2, 344.4, 378.3, 595.6, 457.4])
coinc2 = np.array([608.6, 632.3, 649.7, 663.3, 671.5])
#coinc_mean1 = np.mean(coinc1)
#coinc_max = np.max(coinc)
#print(coinc_mean)
plt.scatter(alt1, coinc1, color = 'blue', alpha = 0.4, s = 500, label = 'Altitude')
plt.legend()

plt.title("Muon counts - Altitude")
plt.savefig("Altitude_Plot.png")

plt.show()


