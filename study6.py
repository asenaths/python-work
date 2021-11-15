age1 = input("age1:  ")
age2 = input("age2:  ")
age3 =  input("age3:  ")
try:
    age1 = int(age1)
    age2 = int(age2)
    age3 = int(age3)
    if age1 > age2 and age1 > age3:
        print ("age1  is the oldest  " )
    elif age2 > age1 and age2 > age3:
        print( "age2 is the oldest")
    elif age1 < age2 and age3:
        print(" age1 is the youngest")
    elif age2 < age1 and age3:
        print("age2 is the youngest")
    else:
        print("age3 is the oldest")
except:
    print("input intergers only")