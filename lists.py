Thelist = list()
while True:
    number = input('number:  ')
    if number == "done":
        break
        try:
            number = int(number)
        except:
            print('invalid input')      
            continue
    Thelist.append(number)

def maximum(values):
    largest = None
    for value in values:
        if largest is None or value > largest:
            largest = value
            return largest
def minimum(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value 
            return smallest
def maxmin(val):
        print("the maximum", maximum)     
        print("the minimum", minimum)

maxmin(Thelist)
