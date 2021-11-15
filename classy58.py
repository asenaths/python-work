import math

print("python calculator and an operator either + - *  / or %")
number = float(input("number:   "))
number2 = float(input("number2:  "))
op = input("operator:  ")
 
def addition(number, number2):
    addition = number + number2
    return addition
    
def subtraction(number,number2):
    subtraction = number - number2
    return subtraction

def multiplication(number, number2):
    multiplication = number * number2
    return multiplication

def division(number,number2):
    division = number/number2
    return division

def modulus(number,number2):
    modulus = number % number2 
    return modulus

def calc(number,number2,operation):

    if  operation == "+":
        print(addition(number,number2))
    elif operation == "-":
        print(subtraction(number,number2))
    elif operation == "*":
        print(multiplication(number,number2))
    elif operation == "/":
        print(division(number,number2))
    else: 
        print(modulus(number,number2))

calc(number,number2,op)        
       
    
