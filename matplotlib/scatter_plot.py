import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng() #random number generator

x_data = rng.random(500) * 100   #generating array of 50 elements between 0 and 100
y_data = rng.random(500) * 100   

plt.scatter(x_data,y_data ,c="red",alpha=0.5)
plt.show()