import math 

print("this program is works as a subtration and addition calculator")
print("input the first and second number and input and operation either + or -")
number = int(input("number:  "))
number1 = int(input("number2:   "))
op = input("operator: ")

 
def subtraction(num,number2): 
    subtraction = num- number2
    return subtraction

# sub = subtraction(num,num2)
def addition(num, num1):
    add = num + num1
    return add
def calc(num, num1, operation):
    if operation == "+":
        print(addition(num, num1))
    else:
        print(subtraction(num,num1))

calc(number, number1, op)
print("+","-")