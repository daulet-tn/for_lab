#1
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kivi"
x = tuple(y)
print(x)
#2
b = list(x)
b.append("orange")
x = tuple(b)
print(x)
#3
b = ("melon",)
x = x + b
print(x)
#4
z = list(x)
z.remove("apple")
x = tuple(z)
print(x)
#5
del x
print(x)
