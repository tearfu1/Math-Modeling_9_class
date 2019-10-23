import numpy as np
from const import svobodnoe_padenie as g
x = 0
y = 0
x0 = 1
y0 = 1
v0 = 1
time = np.arange(0, 5, 0.1)
N = len(time)

a=np.ndarray(shape=(N,3))
for i in range(0, N, 1):
    x = x0+v0*time[i]
    y = y0 + v0*time[i] - (g*(time[i])**2/2)
    a[i][0]=time[i]
    a[i][1]=x
    a[i][2]=y
print(a)