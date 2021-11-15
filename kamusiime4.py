import math 

radius = float(input("radius:  "))
pie = math.pi
nn = 2
def circumference(rad):
    circumference =  nn * pie * rad**2
    return circumference

ans = circumference(radius)
print(ans)