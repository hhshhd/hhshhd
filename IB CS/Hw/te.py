class Student:
    ''' Name : student
        attributes : name, age, gender, class, subjects, grades)
        methods:
        get & set each attributes
        show grade level
        subclass: IBstudent

    '''
    def __init__(self, name="hhs", age=16, gender="M", class_="s2c7", subjects=["Math","Eng","Man","CS","Econ","Phy"], grades=[90,90,80,99,99,80]):
        self.name = name
        self.age = age
        self.gender = gender
        self.class_ = class_
        self.subjects = subjects
        self.grades = grades
        self.avgGrade = 0.0
        self.gradeLevel = ''
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getGender(self):
        return self.gender
    
    def getClass_(self):
        return self.class_
    
    def getSubjects(self):
        return self.subjects
    
    def getGrades(self):
        return self.grades
    
    def setName(self):
        self.name = name
        
    def setAge(self,age):
        self.age = age
        
    def setGender(self):
        self.gender = gender
        
    def setClass_(self):
        self.class_ = class_
        
    def setSubjects(self,subjects):
        self.subjects = subjects
        
    def setGrades(self,grades):
        self.grades = grades
        
    def avgGrades(self):
        self.avgGrade = float(sum(self.grades)/len(self.grades))
        return self.avgGrade
        
    def showGradeLevel(self):
        self.avgGrades()
        list1 = ['F', 'E', 'D', 'C', 'B', 'A']
        self.gradeLevel = list1[int(self.avgGrade//(100/6))]
        return self.gradeLevel
            
    def __str__(self):
        outputStr = ""
        outputStr += "Student Name:" +self.getName() +"\n"
        outputStr += "Student Age:"+str(self.getAge())+"\n"
        outputStr += "Student Gender:" + str(self.getGender())+"\n"
        outputStr += "Student Class:"+ self.getClass_()+'\n'
        outputStr += "Student Subjects:"+ str(self.getSubjects())+'\n'
        outputStr += "Student Subject Scores:"+ str(self.getGrades())+'\n'
        outputStr += "Student Subject Average:" + str(int(self.avgGrades()))+'\n'
        outputStr += "Student Avg Grade:"+self.showGradeLevel()+"\n"
        return outputStr
##class IBStudent(Student):
##    def __init__(self, IBgrades=7, Teacher=['Sam','Atic','Ms.Zhu','Ms.Wu','Mr.Bosss','Kaluosi']):
##
##        self.IBgrades = IBgrades
##        self.Teacher = Teacher
##        self.dielevel = 0.0
##        self.sleep = 0.0
##
##    def getIBgrades(self):
##        return self.IBgrades
##
##    def getTeacher(self):
##        return self.Teacher
##
##    def dielevel(self):
##        self.dielevel = float(Student.avgGrade)
##        return dielevel
##
##    def sleep(self):
##        self.dielevel()
##        self.sleep = float(6*self.dielevel/100)
##        return self.sleep
##
##    def sleep(self):
##        return self.sleep
    
Stu1 = Student("Hanbo")
Stu1.setGrades([0,0,0,0,100,0])
Stu2 = Student()

stuList = [Stu1,Stu2]
for i in range(len(stuList)):
    print("student:",i+1)
    print(stuList[i])
    print("the avarage grade:")
    print(stuList[i].avgGrades())
    print("\n")
    
