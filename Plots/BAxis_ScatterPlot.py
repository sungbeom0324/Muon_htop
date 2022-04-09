#Scattering Plot. Size = coinc / x = latitude , y = altitude
import numpy as np
import matplotlib.pyplot as plt 

alt1 = np.array([30.0, 50, 60, 74, 100, 836])
alt2 = np.array([19, 36, 59, 67, 60])
lat1 = np.array([37.56, 37.56, 37.56, 37.56, 37.56, 37.66])
lat2 = np.array([33.45, 34.30, 35.14, 35.14, 36.32])
coinc1 = np.array([568.2, 344.4, 378.3, 595.6, 457.4, 522.1])
coinc2 = np.array([608.6, 632.3, 649.7, 663.3, 671.5])

f, (ax, ax2) = plt.subplots(2, 1, sharex=True)
ax.plot(coinc1)
ax2.plot(coinc1)
ax.set_ylim(700, 900)  # outliers only
ax.set_xlim(33, 38)  # outliers only
ax2.set_ylim(0, 150)  # most of the data
ax2.set_xlim(33, 38)  # most of the data

# hide the spines between ax and ax2
ax.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax.xaxis.tick_top()
ax.tick_params(labeltop=False)  # don't put tick labels at the top
ax2.xaxis.tick_bottom()

#coinc_mean1 = np.mean(coinc1)
#coinc_max = np.max(coinc)
#print(coinc_mean)

d = .015  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal

plt.scatter(lat1, alt1, color = 'red', alpha = 0.4, s = coinc1, label = 'Altitude')
plt.scatter(lat2, alt2, color = 'blue', alpha = 0.4, s = coinc2, label = 'Latitude')
plt.legend()

plt.title("Size of Dot = Relative Muon Counts")
plt.savefig("BrokenAxis_Muon_Location_ScatteringPlot.png")

plt.show()


