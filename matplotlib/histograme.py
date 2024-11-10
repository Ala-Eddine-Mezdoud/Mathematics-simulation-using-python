import numpy as np
import matplotlib.pyplot as plt

ages = np.random.normal(20,1.5,1000)

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.hist(ages)
plt.title("simple histograme")

plt.subplot(1,2,2)
plt.hist(ages,color="red",edgecolor="black")
plt.title("styled histograme")

plt.tight_layout()
plt.show()
