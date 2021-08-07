from math import sin, cos, tan
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


equation1 = input("Please Enter an equation")
# equation2 = equation1.replace('a', 'b')
# equation3 = equation2.replace('b', 't')

a = float(input("Enter 1st point"))
b = float(input("Enter 2nd point"))
print("Please choice one condition :")
choice = input(print("a.Tolerance Value \nb.Iteration cycles"))
if choice == 'a':
    tol = float(input("Enter tolerance Value"))
    i = 1000
if choice == 'b':
    i = int(input("Enter Number of iterations"))
    tol = 0.0001

c = eval(equation1)  # converting given string into equation
d = f_x(equation1, b)  # eval(equation2)
f = 0
e = c * d
error = 1
prev = 0
print("i\t\t\ta\t\tb\t\t\tx\t\tf(x)\terror")
if e < 0:  # if f(a)*f(b) > 0 then end the program because roots does not exist
    for i in range(1, i + 1):
        t = (a + b) / 2
        f = f_x(equation1, t)    # eval(equation3)
        error = abs(abs(t) - abs(prev))

        if i == 1:
            error = 1
        if error < tol:
            print("ERROR reached : {0:.5} /// {1}".format(error, f))
            quit()

        else:
            prev = t
            if i == 1:
                error = 0
            if f < 0:
                a = t
            if f > 0:
                b = t

        print("{0}\t{1:.5g}\t\t\t\t{2:.4g}\t\t\t\t\t{3:.4g}\t\t\t\t\t\t{4:.4g}\t\t\t\t\t\t\t\t\t{5:.4g}".format(i,
                                                                                                                float(
                                                                                                                    a),
                                                                                                                float(
                                                                                                                    b),
                                                                                                                float(
                                                                                                                    t),
                                                                                                                float(
                                                                                                                    f),
                                                                                                                float(
                                                                                                                    error)))

    else:
        print("{}".format(e))
else:
    print("BITCHHHH")
