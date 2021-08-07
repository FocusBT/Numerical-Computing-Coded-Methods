import math


def u_cal(u, n):
    temp = u
    for i in range(1, n):
        temp = temp * (u - i)
    return temp


n = int(input("Enter value for n : "))
x = [0] * n
y = [[0 for i in range(n)] for j in range(n)]

# for i in range(0, n):
#    x[i] = input("Enter value for x[{0}] : ".format(i))
# for i in range(0, n):
#    y[i][0] = input("Enter value for y[{0}] : ".format(i))

x = [1791, 1801, 1811, 1821, 1831]
y[0][0] = 48
y[1][0] = 65
y[2][0] = 71
y[3][0] = 83
y[4][0] = 96

estimate = float(input("Enter value to be estimated from given data : "))
h = float(x[1] - x[0])  # calculating h
u = float((estimate - x[0]) / h)
tot = y[0][0]


# creating table
for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

# printing table
for i in range(n):
    print(x[i], end="\t")
    for j in range(n - i):
        print(y[i][j], end="\t")
    print("")


for i in range(1, n):
    tot = tot + (u_cal(u, i) * y[0][i]) / math.factorial(int(i))

print("Estimated value of {0} is = {1}".format(estimate, tot))