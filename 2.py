import matplotlib.pyplot as plt
import numpy as np

def prb_and_hprb_plotter (a=1, b=1,c=0, k=1):
    '''воспроизвдение парабол
    и гипербол на одном графике'''
    x=np.arange(-10,10,0.01)
    y=a*x**2+b*x+c
    plt.plot(x, y, label = "prb")
    
    
    x=np.arange(0.01,10,0.01)
    y=k/x
    plt.plot(x,y, color="k", label="hprb")
    
    x=np.arange(-10,-0.01,0.01)
    y=k/x
    plt.plot(x,y, color="k",)
    plt.legend()
    
    plt.show()
prb_and_hprb_plotter()