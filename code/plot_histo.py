import numpy as np
import matplotlib.pyplot as plt

data = [22,20,22,20,20,22,24,23,22,21,20]
counts, bins = np.histogram(data)
print(counts)
print(bins)
plt.hist(bins[:-1], bins, weights=counts)
plt.show()