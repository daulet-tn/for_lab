#1
import math

def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)

degrees = float(input("Inout degree: "))
radians = degrees_to_radians(degrees)
print("Output radian: ", radians)
#2
h = int(input("Height: "))
a = int(input())
b = int(input())
c = ((a + b)/2)*h
print(c)
#3
import math

def regular_polygon_area(n, s):
    if n < 3:
        raise ValueError("A polygon must have at least 3 sides")
    
    area = (n * s ** 2) / (4 * math.tan(math.pi / n))
    return area
15
try:
    n = int(input("Enter the number of sides: "))
    s = float(input("Enter the length of each side: "))
    print(f"The area of the polygon is: {regular_polygon_area(n, s):.2f}")
except ValueError as e:
    print("Error:", e)
#4
def audan(q, w):
    print(q * w)
q = int(input())
w = int(input())
audan(q, w)

