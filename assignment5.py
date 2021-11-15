salary = input("salary:  ")
age = input("age:  ") 
years_of_experience = input("years_of_experience:   ")
try :
    salary = int(salary)
    age = float(age)
    years_of_experience = int(years_of_experience)
    if age >= 60 and years_of_experience >= 10:
        salary = (salary * 0.5 + salary )
        print(salary)
    elif age >= 45 and years_of_experience >= 5 :
        salary = (salary * 0.3 + salary)
        print(salary)
    elif age > 25 and years_of_experience > 3 :
        salary = (salary * 0.15 + salary )
        print(salary)
    else:
        print(salary)
except:
    print("out of range")                        
               
            
        

          
                           
        
         
        
      
           
         
             
   
   
 