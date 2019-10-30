import numpy as np

def progressia (array):
    '''Функция перемножает все элементы массива 
    '''
    
    s = 1
    for a in range(0, len(array), 1):
        s*=s*array[a]
    
    print(s)
progressia([1,2,3,4,5])