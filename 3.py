import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3

fig = plt.figure()
ax = p3.Axes3D(fig)

fi=np.linspace(-2*np.pi,2*np.pi,100)
theta=np.linspace(-2*np.pi, 2*np.pi,100)

h=np.pi

x=np.outer(fi,np.cos(theta))
y=np.outer(fi,np.sin(theta))
z=h*np.outer(np.ones(np.size(fi)),theta)

ax.plot_surface(x,y,z, color='b')

plt.show()


