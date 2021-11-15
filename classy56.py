import math

radius = float(input("radius:  "))
pie = math.pi
ssd = 4/3
def volumeOfSphere(rad):
    volume = ssd * pie * rad**3
    return volumeOfSphere

ans = volumeOfSphere(radius)
print(ans)
