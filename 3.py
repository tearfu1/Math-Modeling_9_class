import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0,100011, 100)

def speed_func(v,t):
    dvdt =(F-k*v**2)/m
    return dvdt
    
v_0 = 500
k = 0.01
F = 1000
m=100000

solve = odeint(speed_func,v_0,t)
plt.plot(t,solve[:,0])
plt.show()