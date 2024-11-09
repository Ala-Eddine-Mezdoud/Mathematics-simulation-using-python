import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
rng = np.random.default_rng()

def bernoulli(p,U):
    return (U < p) # if u < p  it returns 1 , 1 => H otherwhise  0 => T



n = 1000
U = rng.random(n)
toss = bernoulli(0.5 ,U)

avg = [sum(toss[:i])/i for i in range(1,n+1)]
plt.xlabel("number of tosses")
plt.ylabel("probability")

plt . axis([0,n,0,1])
plt . plot(range(0,n) , avg)

plt.show()