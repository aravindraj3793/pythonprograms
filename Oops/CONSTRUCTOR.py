#Constructor
#definition:  to define value(instance variable) in object

class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name,self.age,self.place)

pe1=Person("aravind",22,"wayanad")    #here we can define values in object becoz of using constructor
pe1.printvalue()

pe2=Person("Aswant",23,"Kozhikode")
pe2.printvalue()
