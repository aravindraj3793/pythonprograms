
class Student:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

    def printstu(self):
        print(self.name,self.age,self.place)


f=(open("../INHERITANCE WITH CONSTRUCTOR/student", "r"))
for i in f:
    data=i.strip("\n").split(',')
    stu=Student(data[0],data[1],data[2])
    stu.printstu()
