# fname = input("enter a file name: ")
# fhand = open(fname)
# count = 0
# for line in fhand:
#     count = count + 1
# print("line count",count)

fname = input("enter a file name: ")
fhand  = open(fname)
count = 0
for line in fhand:
    if line.startswith("To:"):
        count = count +  1
        print(count)
        print(line)
