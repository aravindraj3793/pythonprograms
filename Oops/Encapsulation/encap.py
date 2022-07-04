#Encapsulation

# __variable or __methodname this is we use for make variable private



class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.__rollno=rollno
    def printstu(self):
        print(self.name,self.__rollno)

class Emplyee(Student):
    def __init__(self,designation,place):
        self.designation=designation
        self.place=place
    def printemp(self):
        print(self.designation,self.place)
ob=Student('aravind',12)
ob1=Emplyee("Python",'wayanad')
ob1.printemp()
ob1.printstu()

#here __rollno is private it can be only assign from its class only