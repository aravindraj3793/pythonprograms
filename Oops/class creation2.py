class Person:
    def setvalue(self,name,age,place):
#we can only use arguments only in one method
#if we want to use arguments in next methods we use self argument(instance argument)
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name)
        print(self.age)
        print(self.place)

pe1=Person()
pe1.setvalue("Anu",25,"Kochi")
pe1.printvalue()

pe2=Person()
pe2.setvalue("aravind",22,"chennai")
pe2.printvalue()

pe3=Person()
pe3.setvalue("manu",28,"Kochi")
pe3.printvalue()