hours = input("hours:  ")
minutes = input ("minutes:  ")
try:
    hours = int(hours)
    minutes =int(minutes)
    quotient = hours % minutes 
    print(quotient)
except:
    print("remainder")