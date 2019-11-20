import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

edge=2
fig, ax = plt.subplots()
anim_object, = plt.plot([],[], marker='o')

ax.set_xlim(-10*edge,10*edge)
ax.set_ylim(-edge,edge)

def update (R, t):
    x=R*(np.cos(t))**3
    y=R*(np.sin(t))**3
    return x,y
def animate(i):
    anim_object.set_data(update(R=2, t=i))
    
ani=FuncAnimation(fig, animate, frames=np.arange(0, 100, 0.1), interval = 10)
move=update(R=2, t=np.arange(0, 100, 0.1))
plt.plot(move[0],move[1])

plt.axis('equal')
ani.save('ani2.gif')
