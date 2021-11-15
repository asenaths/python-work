quantity = input("quantity:  ")
try:
    quantity = int(quantity)
except:
    print('please put valid input for quantity')
    quit()

price = quantity * 100

if price > 1000:
    new_price =   price  -  (0.1 * price)
    print('Your discounted price is ', new_price)
else:
    print('your bill is ', price)
