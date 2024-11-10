import numpy as np
import matplotlib.pyplot as plt

x = ["c++","python","javascript","html","css","mysql","php","nodeJs","expressJs"]
y = [5,7,7,8,7,5,3,7,6]

plt.figure(figsize=(15, 6))


plt.subplot(1,2,1)
plt.bar(x,y,color="red")
plt.title("simple bar char")

plt.subplot(1,2,2)
plt.bar(x,y,color="green",align="edge",edgecolor="red",lw=2)
plt.title("barchar with styling")

plt.tight_layout()
plt.show()