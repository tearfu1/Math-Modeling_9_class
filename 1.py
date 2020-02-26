import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation


N = 200
t = np.linspace(0,4.3, N)

a = 1
b = 1
c = 1

g = 9.8

def move_func(s,t):
    x,v_x,y,v_y,z,v_z = s
    
    lam = (g-(v_x**2/a**2)-(v_y**2/a**2)-(v_z**2/c**2))/((x**2/a**4)+(y**2/b**4)+(z**2/c**4))

    dxdt = v_x
    d2xdt2 = (x/a**2)*lam   
    
    dydt = v_y
    d2ydt2 = (y/b**2)*lam   
    
    dzdt = v_z
    d2zdt2 = -g+(z/a**2)*lam
    
    return dxdt,d2xdt2,dydt,d2ydt2,dzdt,d2zdt2

x0 = 1
v_x0 = 0

y0 = 1
v_y0 = 0

z0 = 1
v_z0 = 0

s0 = x0,v_x0,y0,v_y0,z0,v_z0

sol = odeint(move_func,s0,t)

fig = plt.figure()
ax = p3.Axes3D(fig)
bodys = []
step = int(N/100)

x = sol[:,1]
y = sol[:,2]
z = sol[:,4]
ball,=ax.plot(x,y,z,'o', color = 'r')
line,=ax.plot(x,y,z,'-', color = 'r')

def ani_func(i):
    ball.set_data(x[i],y[i])
    ball.set_3d_properties(z[i])
    
    line.set_data(x[:i],y[:i])
    line.set_3d_properties(z[:i])
    

ax.set_xlim3d([-10, 10])
ax.set_xlabel('x')

ax.set_ylim3d([-10, 10])
ax.set_ylabel('y')

ax.set_zlim3d([-10, 10])
ax.set_zlabel('z')

ani = animation.FuncAnimation(fig,ani_func,100,interval=50)
ani.save('fdsdfsdfsdf.gif')


    