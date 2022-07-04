#class person[name,age,place]
#class student[rollno,dep,college]

class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printper(self):
        print(self.name,self.age,self.place)


class Student(Person):
    def __init__(self,rollno,department,college,name,age,place):
        super().__init__(name, age, place)
        self.rollno=rollno
        self.departmant=department
        self.college=college
    def printstu(self):
        print(self.rollno,self.departmant,self.college)
ob=Student("Aravind",22,"wayanad",7,"python","Luminar")
ob.printper()
ob.printstu()
#in single inheritance with constructor we use super(). to constructor
#arguments of parant class will define in child class here

#single inheritance [super(). child[parent arguments]