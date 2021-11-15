length = input("length:    ")
breadth = input("breadth:  ")
try :
    length = int(length)
    breadth = int(breadth)
    if length == breadth:
        print("a square")
    else:
        print("not a square")
except:
     print("no length")    
