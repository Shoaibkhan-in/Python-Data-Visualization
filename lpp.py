from pulp import *

model=LpProblem(name="small Problem", sense=LpMinimize)

x=LpVariable(name="x", lowBound=0)
y=LpVariable(name="y", lowBound=0)


model +=(x>=6)
model +=(y>=6)
model +=(x+y<=11)

model +=x+y
print(model)
print(model.solve())
print(model.objective.value())
print(x.value())
print(y.value())