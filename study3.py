first = input("first:  ")
second = input("second:  ")
try:
    first = int(first)
    second = int(second)
    if first > second:
        print(first, "is the greatest")
    else:
        print(second, " is the greatest")
except:
    print("not greatest")