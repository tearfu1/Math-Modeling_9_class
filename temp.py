import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation



def diff_func(s, t):
    
    fi, vfi = s
    
    dfidt = -vfi
    dvfidt = (R*l*m*w**2*np.sin(w*t-fi) + g*l*m*np.sin(fi))/(l**2*m)
     
    return (dfidt, dvfidt)

N = 200
t = np.linspace(0,30,N)

g = 9.8
R = 1.5
l = 0.9
w = 0.1
m = 40

fi0 = np.pi/180*90
vfi0 = 1
s0 = fi0,vfi0
    
sol = odeint(diff_func, s0, t)

x1 = R*np.sin(w*t[:])
y1 = -R*np.cos(w*t[:])

x2 = x1 + l*np.sin(sol[:, 0])
y2 = y1 - l*np.cos(sol[:, 0])


fig = plt.figure()
bodys = []
for i in range(1, len(t), 1):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]
    
    body_line, = plt.plot(thisx, thisy, '-o',color = 'r')
    bodys.append([body_line])

ani = ArtistAnimation(fig, bodys, interval=50)
plt.axis('equal')
plt.grid()
ani.save('h1t.gif')