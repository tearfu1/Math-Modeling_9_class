import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

def fbvufbfuivvvyucdvguievu1():
    for i in range (n):
        
        anim_object, = plt.plot(N_x[:i],N_y[:i],'o-')
        anim_list.append([anim_object])

def hz_kak_nazvat(x_centre, y_centre,R,n):
    x=np.zeros(n)
    y=np.zeros(n)
    for i in range(0,n,1):
        alpha=np.linspace(0,2*np.pi,n)
        x[i]=x_centre-R*np.cos(alpha[i])
        y[i]=y_centre-R*np.sin(alpha[i])
    return x,y





a=1
b=1
c=3
n=200
R=3

N_x = np.linspace(-5,5,n)
N_y = a*N_x**2+b*N_x+c

x_centre_move  = np.linspace(-5,5,n)
y_centre_move = a*x_centre_move**2+b*x_centre_move+c

fig = plt.figure()
anim_list = []

for i in range (n):
     x,y = hz_kak_nazvat(x_centre_move[i],y_centre_move[i],R,n)
     circle,=plt.plot(x,y,'g-',lw=2)
     anim_object, = plt.plot(x_centre_move[i],y_centre_move[i],'o-')
     anim_list.append([circle])
     


fbvufbfuivvvyucdvguievu1()
ani = ArtistAnimation(fig,anim_list,interval=50)
plt.axis('equal')    
ani.save('ani1334.gif')
    

    
    
