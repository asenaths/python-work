number = input("number:  ")
try:
    number = int(number)
    if number % 2 == 0 :
        print("even")
    else:
        print("odd")
except:

    print("not an interger")
    
            