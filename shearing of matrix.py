from sympy import *
A=Point(2,3)
print("The shearing in X- direction by factor 3")
print(A.transform(Matrix([[1,3,0],[0,1,0],[0,0,1]])))
print("The shearing in Y- direction by factor 3")
print(A.transform(Matrix([[1,0,0],[3,1,0],[0,0,1]])))