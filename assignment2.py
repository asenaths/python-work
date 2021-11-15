hours = input('hours: ' ) 
rate = input( 'rate: ' )
try:
    hours = int(hours)
    rate = float(rate) 
    if hours >= 40:
        rate = rate + 1.5
        pay = hours * rate 
        print(' pay is')
        print(pay)
    else: 
        pay = hours * rate               
        print(pay)       
except:
    print("only numbers are allowed")
   