#1
def square(n):
    for i in range(1, n +1):
        yield pow(i, 2)
n = 6
for num in square(n):
    print(num)
#2
def even(N):
    for i in range(N+1):
        if i % 2 == 0:
            yield i
N = 13
for i in even(N):
    print(i)
#3
def num(a):
    for i in range(a +1):
        if i % 3 == 0 and i % 4 ==0:
            yield i
a = 90
for i in num(a):
    print(i)
#4
def san(x, y):
    for i in range(x, y):
        for j in range(y + 1):
            if i == pow(j, 2):
                yield i
x = 20
y = 70
for i in san(x, y):
    print(i)
#5
def obr(z):
    for i in range(z, 0, -1):
        yield i
z = 30
for i in obr(z):
    print(i)