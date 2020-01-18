import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def diff_func(z, t):
    y, omega = z
    dy_dt = omega
    domega_dt = -np.sin(y)*omega - 3*y*t - 5
    return dy_dt, domega_dt

t = np.arange(0, 20, 0.01)
y_0 = 0.01
omega_0 = 0.05
z_0 = y_0, omega_0
solve = odeint(diff_func, z_0, t)
plt.plot(t, solve[:,0])
plt.show()
