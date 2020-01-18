import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

S = 5
R = 10
k = 1
m = 2

def diff_func(z, t):
    S, V = z
    dS_dt = V
    dV_dt = -9.8*np.sin(S/R) - k*V / m
    return dS_dt, dV_dt

t = np.arange(0, 50, 0.01)
S_0 = 5
V_0 = 3
z_0 = S_0, V_0

solve = odeint(diff_func, z_0, t)

plt.plot(t, solve[:,1])
plt.show()
