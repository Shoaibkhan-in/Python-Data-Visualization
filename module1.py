from pylab import *
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from pulp import *

'''A=Point(1,0)
B=Point(2,-1)
Q=Segment(A,B)
print(Q.rotate(pi))

p1=Point(0,0)
p2=Point(4,0)
p3=Point(2,4)
T=Triangle(p1,p2,p3)
print(T.is_isosceles())'''

P=Point(4,-2)
print(P.transform(Matrix([[-1,0,0],[0,1,0],[0,0,1]])))
print(P.scale(7,0))
print(P.transform(Matrix([[-1,0,0],[0,1,0],[0,0,1]])))
print(P.transform(Matrix([[0,-1,0],[-1,0,0],[0,0,1]])))