from math import sin, cos, tan
from math import *
import numpy as ap
import math
def f_x(equation1, a):
    if 'ln' in equation1 or 'log' in equation1 or 'e' in equation1:
        equation1 = equation1.replace("ln", "math.log2")
        equation1 = equation1.replace("log", "math.log10")
        equation1 = equation1.replace("e", "math.exp(1)")

    if 'asin' in equation1 or 'acos' in equation1 or 'atan' in equation1 or 'asec' in equation1 or 'acosec' in equation1 or 'acot' in equation1:
        equation1 = equation1.replace("asin", "nisa")
        equation1 = equation1.replace("acos", "soca")
        equation1 = equation1.replace("atan", "nata")
        equation1 = equation1.replace("asec", "cesa")
        equation1 = equation1.replace("acosec", "cesoca")
        equation1 = equation1.replace("acot", "toca")

    if (
            'sin' in equation1 or 'cos' in equation1 or 'tan' in equation1 or 'sec' in equation1 or 'cosec' in equation1 or 'cot' in equation1):
        equation1 = equation1.replace("sin", "math.sin")
        equation1 = equation1.replace("cos", "math.cos")
        equation1 = equation1.replace("tan", "math.tan")
        equation1 = equation1.replace("sec", "math.sec")
        equation1 = equation1.replace("cosec", "math.cosec")
        equation1 = equation1.replace("cot", "math.cot")

    if (
            'nisa' in equation1 or 'soca' in equation1 or 'nata' in equation1 or 'cesa' in equation1 or 'cesoca' in equation1 or 'toca' in equation1):
        equation1 = equation1.replace("nisa", "math.asin")
        equation1 = equation1.replace("soca", "math.acos")
        equation1 = equation1.replace("nata", "math.atan")
        equation1 = equation1.replace("cesa", "math.asec")
        equation1 = equation1.replace("cesoca", "math.acosec")
        equation1 = equation1.replace("toca", "math.acot")
    return eval(equation1)

n = int(input("Enter value for n : "))
x = [0] * n
fx = [0] * n
l = [0] * n

choice = int(input("1. Equation\n2. Enter values"))
degree = int(input("enter degree"))

for i in range(0, n):
    x[i] = input("Enter value for x[{0}] : ".format(i))

if choice == 1:
    equation = input("Enter equation : ")
    for i in range(0,n):
        fx[i] = f_x(equation,x[i])

if choice == 2:
    for i in range(0,n):
        fx[i] = input("Enter value for fx[{0}] : ".format(i))




# x = [2, 2.75, 4]
value = float(input("Enter x value : "))

temp = 1
tot = 0

for i in range(n):
    for j in range(n):
        if j != i:
            temp = float(temp) * (float(value) - float(x[j])) / (float(x[i]) - float(x[j]))
    l[i] = temp
    temp = 1

for i in range(n):
    tot = float(tot) + float(l[i]) * float(fx[i])

print(tot)

quit()

counter = 1
i = 0
j = 1
while i < n:
    m = m + 1
    if j == n:
        print("[ {0} {1} ]".format(i, j))
        i = 0
        counter = counter + 1
        j = counter

    print("[ {0} {1} ]".format(i, j))
    i = i + 1
    j = j + 1

    if counter == n:
        quit()
