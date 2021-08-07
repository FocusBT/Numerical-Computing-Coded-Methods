from math import sin, cos, tan
from math import *
from functools import reduce
import operator
import math
equation1 = input("Please Enter an equation")
equation2 = equation1.replace('a', 'b')
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


print("Enter limits :")
a = float(input("For a = "))
b = float(input("For b = "))
h = (b-a)/2


# c = eval(equation1, {'sqrt': sqrt, 'sin': sin, 'cos': sin, 'tan': sin})
# d = eval(equation2, {'sqrt': sqrt, 'sin': sin, 'cos': sin, 'tan': sin})

c = f_x(equation1, a)
d = f_x(equation1, b)


ans = h*(c+d)

print("Answer : {0}".format(ans))
