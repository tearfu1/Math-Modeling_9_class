import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

G = 6.67 * 10**(-11)
M = 6 * 10**24
k = 1
m = 2

def diff_func(z, t):
    R, V = z
    dR_dt = V
    dV_dt = -G * M / R**2 - k*V / m
    return dR_dt, dV_dt

t = np.arange(0, 50, 0.01)
R_0 = 6400000
V_0 = 200
z_0 = R_0, V_0

solve = odeint(diff_func, z_0, t)

plt.plot(t, solve[:,0])
plt.show()
