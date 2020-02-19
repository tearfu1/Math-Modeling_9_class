import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3

fig = plt.figure()
ax = p3.Axes3D(fig)

fi=np.linspace(0,1.5*np.pi,100)
theta=np.linspace(0, 2*np.pi,100)

x=np.outer(fi,np.cos(theta))
y=np.outer(fi,np.sin(theta))
z=np.outer(fi**2,np.ones(np.size(fi)))

ax.plot_surface(x,y,z, color='b')

plt.show()

