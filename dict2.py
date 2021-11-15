fhand = input("please input your file name :  ")
try:
    fname  = open(fhand)
except:
    print("file not found",fhand)
    exit()
    
    
ase = dict()
for line in fname:
    words = line.split()
    for word in words:
        if word not in ase:
           ase[word] = 1
        else:
            ase[word] =+ 1
rdd  = list(ase.keys())           
list.sort()
print(rdd)            
         
#     words  = line.split()
# rd = list(fname.keys())
# counts.sort()
# counts.append()
# print(rd)
# for line in fname:
#     words = line.split()
#     for word in words:
#         counts.append(word)    
    
    
# counts.sort()    
    #     if word not in counts:
    #         counts[word] = 1
    #     else:
    #         counts[word] =+ 1
# print(counts)        

#     line = words.split()
#     counts = dict()
    
#     for line in words:
#         counts =+ 1
# print(counts)
