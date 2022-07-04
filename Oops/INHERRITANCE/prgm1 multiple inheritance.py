class Person:
    def setper(self,name,age):
        self.name=name
        self.age=age


class Parent:
    def setpar(self,place,phone):
        self.place=place
        self.phone=phone



class Employe(Person,Parent):
    def setemp(self,id,designation,salary):
        self.id=id
        self.designation=designation
        self.salary=salary
        print(self.name,self.age,self.place,self.phone,self.id,self.designation,self.salary)

em=Employe()
em.setper("aravind",22)
em.setpar("wayanad",8945566332)
em.setemp(221,"developer",100000)