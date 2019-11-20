import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

edge=10
fig, ax = plt.subplots()
anim_object, = plt.plot([],[], marker='o')

ax.set_xlim(0*edge,10*edge)
ax.set_ylim(-edge,edge)

def update (R, t):
    x=R*(t-np.sin(t))
    y=R*(1-np.cos(t))
    return x,y
def animate(i):
    anim_object.set_data(update(R=2, t=i))
    
ani=FuncAnimation(fig, animate, frames=30, interval = 10)
move=update(R=2, t=np.arange(0, 100, 0.1))
plt.plot(move[0],move[1])

ani.save('govno.gif')
