import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

R=2
N=100
v=1
x0=0
y0=0


def blablabla (R,N,v):
    
    cordinate =np.ndarray(shape=(N,2))
    velocity = np.ndarray(shape=(N,2))
    
    alpha=360/N
    for i in range(N):
        x=R*np.cos(i*alpha*np.pi/180)
        y=R*np.sin(i*alpha*np.pi/180)
        cordinate[i][0] = x+x0
        cordinate[i][1] = y+y0
        plt.plot(x,y, marker = 'o')
        
        if x<0 and y<0:
            v_x = -v*np.cos(i*alpha)
            v_y = -v*np.sin(i*alpha)
        elif x<0 and y >= 0:
            v_x = -v*np.cos(i*alpha)
            v_y = v*np.sin(i*alpha)
        elif x > 0 and y >= 0 :
            v_x = v*np.cos(i*alpha)
            v_y = v*np.sin(i*alpha)
        elif x > 0 and y < 0:
            v_x = v*np.cos(i*alpha)
            v_y = -v*np.sin(i*alpha)
        
        velocity[i][0] = v_x
        velocity[i][1] = v_y
        
    return cordinate, velocity
c,v        
        
        
    plt.axis('equal')
    plt.show()
    
    
    
blablabla(R,N,v)
    
