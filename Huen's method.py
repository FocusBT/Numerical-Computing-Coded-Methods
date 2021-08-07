from math import sin, cos, tan
from math import *
import numpy as ap
import math

equation = input("Please Enter an equation : ")
h = float(input("Enter h value : "))
print("Enter initial values for x and y ")
x = float(input("for x = "))
y = float(input("for y = "))

print("t's limit : ")
t1 = float(input("for t1 = "))
t2 = float(input("for t2 = "))
n = int(input("Enter value for N : "))
n = n + 1
t = [0] * n
w = [0] * n
n = n - 1
t[0] = x
w[0] = y
temp = x

for i in range(0, n):
    if temp == t2:
        break

    t[i] = temp
    temp = temp + h

i = 0
while t[i] < t2:

    # print("For x = {0} , y = {1}".format(t[i], w[i]))
    a = t[i]
    b = w[i]
    k1 = eval(equation)

    a = t[i] + (1 / 3) * h
    b = w[i] + (1 / 3) * k1 * h
    k2 = eval(equation)  # facing error here

    a = t[i] + (2 / 3) * h
    b = w[i] + (2 / 3) * k1 * h
    k3 = eval(equation)

    w[i + 1] = w[i] + (h / 4) * (k1 + 3 * k3)
    print(w[i + 1])
    if n == i + 1:
        break
    i = i + 1
