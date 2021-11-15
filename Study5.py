marks = input("marks:   ")
try:
    marks = int(marks)
    if marks >= 80:
        print("A")
    elif marks >= 60:
        print("B")
    elif marks >= 50:
        print("c")
    elif marks >= 45:
        print("D")
    elif marks >= 25:
        print("E")
    else: 
        print("F")
except:
     print("improve")




           
      