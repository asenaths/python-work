# number_of_classes_held = input("number_of_classes_held:  ")
# number_of_classes_attended = input("number_of_classes_attended:  ")
# try:
#     number_of_classes_held = int(number_of_classes_held)
#     number_of_classes_attended = int(number_of_classes_attended)
   
#     percentage_attendance = (number_of_classes_attended/number_of_classes_held) * 100
    
#     if percentage_attendance < 75.0:
#         print("you will not sit for exams because your attendance is ", percentage_attendance, '%')
#     print("get ready for exam")
# except:
#     print("only intergers are allowed")

def showEmpoyee(name, salary = 9000):
    print(name, salary)

showEmpoyee("Ronnie", 10)