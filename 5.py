from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation

fig=plt.figure()
ax=p3.Axes3D(fig)

fig = plt.figure()
ax = p3.Axes3D(fig)

fi=np.linspace(-2*np.pi,2*np.pi,100)
theta=np.linspace(-2*np.pi, 2*np.pi,100)

h=np.pi

x=np.outer(fi,np.cos(theta))
y=np.outer(fi,np.sin(theta))
z=h*np.outer(np.ones(np.size(fi)),theta)

ax.plot_surface(x,y,z, color='b')



x=fi* np.cos(theta)
y=fi * np.sin(theta)
z=h*theta

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
