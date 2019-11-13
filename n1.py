import matplotlib.pyplot as plt

def cube_plotter (a):
    '''рисовалка кубов'''    
    b = a + 0.5
    
    plt.plot([a,a,a+a,a+a,a], [a,a+a,a+a,a,a], color="k")
    plt.plot([a,b,b,a+b,a+b,a+b,a+a],[a+a,a+b,a+b,a+b,a+b,b,a],color="k")
    plt.plot([a+a,a+b],[a+a,a+b],color="k")
    plt.plot([b,b,a+b],[a+b,b,b],linestyle='--',linewidth=1.5,color="k")
    plt.plot([a,b],[a,b],linestyle='--',linewidth=1.5,color="k")
    plt.axis('equal')

    plt.show()
    
cube_plotter(2)
