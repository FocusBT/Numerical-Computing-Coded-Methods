import math

equation1 = input ("Enter any equation ")


def f_x (equation1, a):
    if 'ln' in equation1 or 'log' in equation1 or 'e' in equation1:
        equation1 = equation1.replace ("ln", "math.log2")
        equation1 = equation1.replace ("log", "math.log10")
        equation1 = equation1.replace ("e", "math.exp(1)")

    if 'asin' in equation1 or 'acos' in equation1 or 'atan' in equation1 or 'asec' in equation1 or 'acosec' in equation1 or 'acot' in equation1:
        equation1 = equation1.replace ("asin", "nisa")
        equation1 = equation1.replace ("acos", "soca")
        equation1 = equation1.replace ("atan", "nata")
        equation1 = equation1.replace ("asec", "cesa")
        equation1 = equation1.replace ("acosec", "cesoca")
        equation1 = equation1.replace ("acot", "toca")

    if (
            'sin' in equation1 or 'cos' in equation1 or 'tan' in equation1 or 'sec' in equation1 or 'cosec' in equation1 or 'cot' in equation1):
        equation1 = equation1.replace ("sin", "math.sin")
        equation1 = equation1.replace ("cos", "math.cos")
        equation1 = equation1.replace ("tan", "math.tan")
        equation1 = equation1.replace ("sec", "math.sec")
        equation1 = equation1.replace ("cosec", "math.cosec")
        equation1 = equation1.replace ("cot", "math.cot")

    if (
            'nisa' in equation1 or 'soca' in equation1 or 'nata' in equation1 or 'cesa' in equation1 or 'cesoca' in equation1 or 'toca' in equation1):
        equation1 = equation1.replace ("nisa", "math.asin")
        equation1 = equation1.replace ("soca", "math.acos")
        equation1 = equation1.replace ("nata", "math.atan")
        equation1 = equation1.replace ("cesa", "math.asec")
        equation1 = equation1.replace ("cesoca", "math.acosec")
        equation1 = equation1.replace ("toca", "math.acot")
    return eval (equation1)


equation2 = equation1.replace ('a', 'b')
equation3 = equation2.replace ('b', 't')

a = float (input ("Enter 1st point"))
b = float (input ("Enter 2nd point"))

choice = input (print ("a.Tolerance Value\nb.Iteration cycles"))
if choice == 'a':
    tol = float (input ("Enter tolerance Value"))
    i = 1000
if choice == 'b':
    i = int (input ("Enter Number of iterations"))
    tol = 0.0001

c = f_x (equation1, a)
d = f_x (equation1, b)
prev = 0
e = c * d
e = -1
print ("i\t\t\tx\t\t   f(x)")
prev = b
if e < 0:
    for i in range (1, i + 1):
        c = f_x (equation1, a)  # f(a)
        d = f_x (equation1, b)  # f(b)

        t = (a * d - b * c) / (d - c)  # x
        f = f_x (equation1, t)  # f(x)
        error = float (((t) - (prev)))

        print ('{:<10d}{:^10f}{:>10f}{:>10f}'.format (i, float (t), float (f),float(error)))

        a = b
        b = t

        prev = t
        if i == 0:
            error = 1
        if abs(error) < tol:
            quit ( )
