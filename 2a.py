import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint

t=np.arange(10**(-7),1.1*10**(-7),10**(-11))

def move_func(s,t):
    x,v_x,y,v_y,z,v_z=s
    dxdt=v_x
    dv_xdt=q/m*(Ex+v_y*Bz-v_z*By)
    dydt=v_y
    dv_ydt=q/m*(Ey+v_z*Bx-v_x*Bz)
    dzdt=v_z
    dv_zdt=q/m*(Ez+v_x*By-v_y*Bx)
    return dxdt,dv_xdt,dydt,dv_ydt,dzdt,dv_zdt

x0=0
v_x0=10**7

y0=0
v_y0=10**6

z0=0
v_z0=0

s0=x0,v_x0,y0,v_y0,z0,v_z0

q=1.6*10**(-19)
m=1.67*10**(-31)

Ex=0
Ey=10**(-3)
Ez=0

Bx=10**(-3)
By=10**(-3)
Bz=10**(-3)

sol=odeint(move_func,s0,t)

fig = plt.figure()
ax=fig.gca(projection='3d')

ax.plot(sol[:,0],sol[:,2],sol[:,4], label='dadada')

ax.quiver(x0,y0,z0,Bx,By,Bz,length=(sol[len(t)-1,4]
-sol[0,4]),normalize=True,color='r',label='b')

ax.quiver(x0,y0,z0,Ex,Ey,Ez,length=(sol[len(t)-1,4]
-sol[0,4]),normalize=True,color='g',label='v')

ax.quiver(x0,y0,z0,v_x0,v_y0,v_z0,length=(sol[len(t)-100,4]
-sol[0,4]),normalize=True,color='g',label='v')


ax.legend()

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title('neponyatnaya krivaya')

plt.show

