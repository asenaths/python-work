salary = input("salary:  ")
Years_of_service = input("years_of_service:  ")
try:
    salary = int(salary)
    Years_of_service = int(Years_of_service)
except:
    print("pLEASE INPUT ONLY VALID VALUES")  
    quit()

if Years_of_service >= 5:
    salary = (salary * 0.05 + salary)
    print("your new salary is ", salary)
else:
    print(salary)

