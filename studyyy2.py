import math
import random 
print("this program shows whether the generated numbers are either greater, less or equal ")
number = input("number:  ")
Y = random.randint(2,5)
try:
    number = int(number)
    if number > Y:
        print("the value is  greater")
    elif number < Y:
        print("the value  is less")
    else :
        print("the value is equal")
except:
            print ("floating numbers are not  allowed")

