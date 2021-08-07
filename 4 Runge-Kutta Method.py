from math import sin, cos, tan
from math import *
import numpy as ap
import math


equation = input("Please Enter an equation : ")
# equation = "b-a*a+1"
h = float(input("Enter h value : "))
print("Enter initial values for x and y ")
x = float(input("for x = "))
y = float(input("for y = "))
# h = 0.2
# x = 0
# y = 0.5

print("t's limit : ")
t1 = float(input("for t1 = "))
t2 = float(input("for t2 = "))
# t1 = 0
# t2 = 2

n = int(input("Enter value for N : "))
# n = 10
n = n + 1
t = [0]*n
w = [0]*n
n = n - 1
t[0] = x
w[0] = y

temp = x

for i in range(0, n):
    if temp == t2:
        break

    t[i] = temp
    temp = temp + h

# for i in range(0, n):
#    print("For x = {0} , y = {1}".format(t[i], w[i]))

i = 0
while t[i] < t2:

    # logical error here

    print("For x = {0} , y = {1}".format(t[i], w[i]))
    a = t[i]
    b = w[i]
    k1 = h * eval(equation)

    a = t[i] + (h/2)
    b = w[i] + (1/2)*k1
    k2 = h * eval(equation)    # facing error here

    a = t[i] + (h/2)
    b = w[i] + (k2/2)
    k3 = h * eval(equation)

    a = t[i+1]
    b = w[i] + k3
    k4 = h * eval(equation)

    w[i+1] = w[i] + (1/6)*(k1+2*k2+2*k3+k4)
    print(w[i+1])
    if n == i+1:
        break
    i = i+1
# need working here

# print("{0}\n\n\n\n\n{1}".format(t[i], w[i]))