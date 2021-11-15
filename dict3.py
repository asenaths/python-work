# eng2rr = dict()
# eng2rr["two"]  = "ibiri" 
# eng2rr["three"] = "ishatu"
# eng2rr["four"] = "ina"
# print(eng2rr["three"])



name = input("input your file name:  ")
try:
    num = open(name)
except:
    print("your file not opened",name)
    exit()
    
    
rdd = dict()
for line in num:
  words = line.split()


if "tum" in words:
  print("is there")  
else:
  print("is not")
