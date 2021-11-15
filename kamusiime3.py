celsius = input("input temperatures in celsius:  ")
try :
    celsius = float(celsius)
    kelvin(celsius)
    fahrenheit(celsius) 

except:    
    print("please input only intergers or floating numbers ")

def kelvin(temperature):
    kelvin =  temperature + (273.15)
    print(kelvin)

def fahrenheit(temperature):
    fahrenheit = temperature * (9/5) + 32
    print(fahrenheit)

