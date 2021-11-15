import math

num = 3/4
pie  = math.pi
radius = int(input("radius:  "))
height = int(input("height:   "))

def area_of_sphere(rad,height):
    area = num * pie * (rad**2) * height
    return area
answer  =   area_of_sphere(radius,height)
print(answer)

