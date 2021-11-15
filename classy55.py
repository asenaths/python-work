import math

print("this program is a multiplication and  a subtraction calculator")
print(" input the first and the second number and the operation either * or -")
number1 = int(input("number1:   "))
number2 =int(input("number2:  "))
op = input('operator:  ' )

def multiplication(number1,number2):
    mult = number1 * number2
    return mult

# mult = multiplication(number1, number2)
def subtraction(number1, number2):
   sub = number1 - number2
   return sub

def calc(number1, number2, operation ) :
    if operation ==  "*" :
        print(multiplication(number1, number2))
    else:
      print(subtraction(number1 , number2))

calc(number1, number2, op)

