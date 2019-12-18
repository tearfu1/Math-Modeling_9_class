import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


t = np.arange(0,8, 0.02)


def bucks_func(n,t):
    dndt=-k*n*t
    return dndt

n_0 = 1000
k = 0.08

solve = odeint(bucks_func,n_0,t)
plt.plot(t,solve[:,0], label = 'Количетсво бактерий')
plt.show()