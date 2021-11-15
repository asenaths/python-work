# stuff  = list()
# dir()class PartyAnimal:
# class partyAnimal:
#     x = 0
    
# def party(self) :
#     self.x = self.x + 1
#     print("So far",self.x)
# party('self')
# an = partyAnimal()
# an.party()
# an.party()
# an.party()
# partyAnimal.party(an)

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def getName(self):
        return self.name



class courses:

    def __init__(self,name,code,max):
        self.courseName = name
        self.courseCode = code
        self.StdNumber = max
        self.students = []
        
    def getCode(self):
        return self.courseCode

    def addStudent(self, student):
        if len(self.students) < self.StdNumber:
            self.students.append(student)
            print(student.getName(), " has been successfull enrolled to the course")
        else:
            print("cannot add student because the course is full")
        
        
std1 = student("Ronnie", 25)
std2 = student("Asenaths", 15)
std3 = student("Rogers", 5)

It = courses("Computer Science", "CS001", 2)
It.addStudent(std1)
It.addStudent(std2)