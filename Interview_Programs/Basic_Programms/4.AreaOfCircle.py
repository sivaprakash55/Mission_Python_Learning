# To find area of a circle

from math import pi
def area(r):
    return pi*pow(r,2) if r !=0 else 0

radius = float(input("Enter radius of the circle : "))
print(f"Area of the Circle is {area(radius)}")