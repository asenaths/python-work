fhand =open("text1.txt")
for line in fhand:
    line = line.rstrip()
    line = line.upper()
    print(line)