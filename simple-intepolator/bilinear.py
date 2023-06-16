import matplotlib.pyplot as plt
import numpy as np
import functools
import math
from stylizer import f_as_text

data = [(-1,5,3),(3,6,7),(6,-7,3),(3,-9.5,5),(3,-7.1,0),(-4.6,7,1.8),(3.9,5.2,-5.9),(3.6,2.7,6.1),(-2.5,7.4,3.9),(5.8,-4.1,9.2)]

rank = math.ceil(len(data)**0.5)-1
power_touples = [[i, j] for i in range(rank+1) for j in range(rank+1)]

def power_values(x, y):
    return [x**p_t[0]*y**p_t[1] for p_t in power_touples]

A = [power_values(touple[0], touple[1]) for touple in data]
At = np.transpose(A)
f = list(map(lambda touple : touple[2], data))

b = np.linalg.solve(np.matmul(At, A), np.matmul(At, f))

def f(x, y):
    return sum([b[i]*x**powers[0]*y**powers[1] for i, powers in enumerate(power_touples)])

def get_f(accuracy=-1):
    return f_as_text(b, power_touples,accuracy)

print(get_f(2))

# - - - - - - - -

kpu = 50

def bound(f, axis_id):
    return functools.reduce(lambda acc, touple : f(touple[axis_id], acc), data, data[0][axis_id])

X = np.outer(np.linspace(bound(min, 0), bound(max, 0), kpu), np.ones(kpu))
Y = np.outer(np.linspace(bound(min, 1), bound(max, 1), kpu), np.ones(kpu)).T
Z = f(X, Y)
ax = plt.axes(projection ='3d')
ax.plot_surface(X, Y, Z)
[ax.scatter(touple[0], touple[1], touple[2]) for touple in data]
plt.show()