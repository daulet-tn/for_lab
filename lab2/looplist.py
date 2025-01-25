mylist = ["apple", "banana", "cherry", "kivi", "melon", "watermelon"]
for i in mylist:
    print(i)
for i in range(len(mylist)):
    print(mylist[i])
x = 0
while x < len(mylist):
    print(mylist[x])
    x = x + 1
[print(x) for x in mylist]