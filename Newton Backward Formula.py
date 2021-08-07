import math
def u_cal(u, n):
    temp = u
    for i in range(1, n):
        temp = temp * (u + i)
    return temp


n = int(input("Enter value for n : "))
x = [0] * n
y = [[0 for i in range(n)] for j in range(n)]

for i in range(0, n):
    x[i] = input("Enter value for x[{0}] : ".format(i))
for i in range(0, n):
    y[i][0] = input("Enter value for y[{0}] : ".format(i))

estimate = float(input("Enter value to be estimated from given data : "))
h = float(float(x[1]) - float(x[0]))  # calculating h
u = float((float(estimate) - float(x[n-1])) / float(h))
tot = y[n-1][0]
print("{0} and {1}".format(h,u))


# creating table
for i in range(1, n):
    for j in range(n - i):
        y[j][i] = float(y[j + 1][i - 1]) - float(y[j][i - 1])

# printing table
for i in range(n):
    print(x[i], end="\t")
    for j in range(n - i):
        print(y[i][j], end="\t")
    print("")


i = n-2
j = 1

while i >= 0:
    tot = float(tot) + (float(u_cal(u, i)) * float(y[i][j])) / math.factorial(int(i))
    j = j + 1
    i = i - 1

print("Estimated value of {0} is = {1}".format(estimate, tot))
