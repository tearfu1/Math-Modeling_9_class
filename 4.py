import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3

fig = plt.figure()
ax = p3.Axes3D(fig)

fi=np.linspace(-2*np.pi,2*np.pi,100)
theta=np.linspace(-2*np.pi, 2*np.pi,100)

n=1
l=1
m=1
n=1

def fu(par):
    return l*par

x=np.outer(fi,np.cos(theta)) + l*np.outer(np.ones(np.size(fi)),fu(theta))
y=np.outer(fi,np.sin(theta)) + m*np.outer(np.ones(np.size(fi)),fu(theta))
z=n*np.outer(np.ones(np.size(fi)),fu(theta))

ax.plot_surface(x,y,z, color='b')

plt.show()