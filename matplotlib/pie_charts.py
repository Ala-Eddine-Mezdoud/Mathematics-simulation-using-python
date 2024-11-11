import numpy as np
import matplotlib.pyplot as plt

langs = ["Python","C++","PHP","C#","GO"]
votes = [42,10,8,12,20]
explodes = [0,0,0,0.2,0]

plt.figure(figsize=(10,5))
plt.pie(votes,labels=langs,explode=explodes,autopct="%.2f%%",pctdistance=0.8,startangle=80,radius=1.3)
plt.show()