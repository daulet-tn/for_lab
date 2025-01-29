list1 =["apple", "banana", "melon", "watermelon", "kivi"]
list2 = ["mers", "bmw", "tayota", "mazda", "dodge"]
#1
list1.append("limon")
print(list1)
#2
x = list1.copy()
print(x)
#3
print(list1.count("melon"))
#4
list1.extend(list2)
print(list1)
#5
print(list2.index("mazda"))
#6
list1.insert(3, "food")
print(list1)
#7
list2.pop(2)
print(list2)
#8
list1.remove("apple")
print(list1)
#9
list1.sort()
print(list1)
#10
list2.clear()
print(list2)
