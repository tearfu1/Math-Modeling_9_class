import matplotlib.pyplot as plt
import numpy as np

def cir_ell_plotter (R=1.5, a=1, b=2, ttle = "circle and epllipse plotter"):
    '''Рисовалка окружностей и эллипсов'''
    x=np.arange(-2.0, 2.0, 0.1)
    y=np.arange(-2.0, 2.0, 0.1)
    X,Y = np.meshgrid(x,y)
    fxy = X**2 + Y**2
    plt.contour(X,Y, fxy, levels =[R**2])
    
    x=np.arange(-2.0, 2.0, 0.1)
    y=np.arange(-2.0, 2.0, 0.1)
    X,Y = np.meshgrid(x,y)
    fxy = (X**2)/a**2 + (Y**2)/b**2 
    plt.contour(X,Y, fxy, levels =[1])
    plt.grid()
    plt.show
cir_ell_plotter()
    