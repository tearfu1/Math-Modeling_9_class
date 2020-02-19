import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3

fig = plt.figure()
ax = p3.Axes3D(fig)

fi=np.linspace(-2*np.pi,2*np.pi,100)
theta=np.linspace(-2*np.pi, 2*np.pi,100)
a=2
b=5
c=8

x=a*np.outer(np.cos(fi),np.sinh(theta))
y=b*np.outer(np.sin(fi),np.sinh(theta))
z=c*np.outer(np.ones(np.size(fi)),np.sinh(theta))

ax.plot_surface(x,y,z, color='b')

plt.show()


