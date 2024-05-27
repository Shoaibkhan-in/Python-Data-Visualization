from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from sympy import *
from pulp import *
'''x=np.linspace(-10,10)
y=np.linspace(-10,10)
def f(x,y):
    return np.sin(x)+np.cos(x)

X,Y=meshgrid(x,y)
Z=f(X,Y)
ax=axes(projection="3d")
ax.contour3D(X,Y,Z,100)
xlabel("x")
ylabel("y")
title("3D Graph sin(x)+cos(x)")
show()
x=np.linspace(-1,1)
y=np.arcsin(x)
plot(x,y,color="r", ls="--",label="$sin^-1*x$")
xlabel("x")
ylabel("y")
title("2D Graph")
legend()
show()

A=Point(1,0)
B=Point(2,-1)
L=Segment(A,B)
M=L.rotate(pi/2)
print(M)'''
'''P=Point(5,2)
Q=Point(5,-2)
R=Point(5,0)
print(P.are_coplanar(Q))
S=Ray((5,2),(5,-2))
print(S.length)
print(S.slope)
'''
'''model=LpProblem(name="small problem", sense=LpMaximize)

x=LpVariable(name="x", lowBound=0)
y=LpVariable(name="y", lowBound=0)

model += (4*x+6*y<=24)
model += (5*x+3*y<=15)
model += 150*x+75*y

print(model)
print(model.solve())
print(model.objective.value())
print(x.value())
print(y.value())'''

'''x=Point(2,-4)
t=x.transform(Matrix([[1,0,0],[0,-1,0],[0,0,1]]))
print(t)
print(x.scale(6,0))
s=x.transform(Matrix([[1,3,0],[0,1,0],[0,0,1]]))
print(s)
p=x.rotate(pi/6)
print(p)
'''
A=Point(3,2)
B=Point(2,-3)

a=Matrix([[cos(pi/6),sin(pi/6),0],[-sin(pi/6), cos(pi/6), 0],[0,0,1]])
b=Matrix([[1,0,0], [0,-4,0],[0,0,1]])
c=Matrix([[-6.4,0,0],[0,-6.4,0],[0,0,-6.4]])
d=Matrix([[1,0,0],[5,1,0],[0,0,1]])
E=a*b*c*d
print(E)
s=Matrix([[3,2,0],[2,-3,0],[0,0,1]])
t=s*E
print(t)
s.transform(Matrix(E))