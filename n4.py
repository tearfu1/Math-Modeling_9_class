from const import c
from const import vo
from const import plotnost as ro



def boom(ma, v):
    """Последвствия столькновения
    """
    m = vo * ro
    delta = ((m*v**2)/2)/(2*c*m)
    if delta >=50:
        print('all decay')
    elif delta >=30 and delta <=50:
        print('90% died')
    elif delta >= 30:
        print("bol'no")
    else:
        print("n143g0")
        print(speed(ma))

def speed(ma, m=vo*ro):
        speed=((2*c*50*m)/m)**0.5
        return speed
boom(ma=1**20, v=1) 
        
    

    
    
