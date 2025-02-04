#1
x = ("apple", "banana", "cherry")
print(x)
#2
(green, yellow, red) = x
print(green)
print(yellow)
print(red)
#3
x = ("apple", "banana", "cherry", "kivi", "melon")
(green, yellow, *red) = x
print(green)
print(yellow)
print(red)
#4
x = ("bmw", "mers", "subaru", "dodge", "audi")
(a1, *a2, a3) = x
print(a1)
print(a2)
print(a3)

