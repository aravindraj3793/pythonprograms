#person[name,age,place]
#employee[empid,dep,salary]
#student[rollno,college]

#in multiple inheritance we dont use super in constructor we use class_name.init in here
class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

class Employee():
    def __init__(self,empid,departmant,salary):
        self.empid=empid
        self.departmant=departmant
        self.salary=salary

class Student(Person,Employee):
    def __init__(self,rollno,college,name,age,place,empid,departmant,salary):
        Person.__init__(self,name,age,place)
        Employee.__init__(self,empid,departmant,salary)
        self.rollno=rollno
        self.college=college
    def printstu(self):
        print(self.name,self.age,self.place,self.empid,self.departmant,self.salary,self.rollno,self.college)

stu=Student("Aravind",22,"Wayanad","Emp001","Python",10000,101,"Luminar")
stu.printstu()

#multiple inheritance [classname.init__(self,argument)  child[parent arguments]