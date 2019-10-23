import math
from const import svobodnoe_padenie as g
from const import boltsmans_const as k
from const import planks_const as h1
from math import pi,e

print('№1')
beta = pi/5 
h = 100
alpha = pi/3

v = math.sqrt((g*h*(1/math.tan(beta)**2))/(2*math.cos(alpha)**2*(1-1/math.tan(beta)*1/math.tan(alpha))))
print(v)

print('№2')
t=200
e1=300
N=(2/(math.sqrt(pi))*(h1/(k*t)**1.5)*e**((-e1)/(k*t))*e1**(t/2))
print(N)
