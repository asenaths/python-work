import math

pie = math.pi
radius = int(input("radius:  "))

def area (radius):
    area = pie * radius**2
    return area 


area =  area(radius)
print(area)