kilogram =  input("kilogram:  ")
try:
    kilogram = int(kilogram)
except:
    print("only intergers are allowed")
    quit()

def grammes(k):
    grammes = k * 1000
    return grammes


ans = grammes(kilogram)
print(ans)