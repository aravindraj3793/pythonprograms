class Person:
    def setper(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
        print(self.name,self.age,self.place)

class Student(Person):
    def setstu(self,roll,department):
        self.roll=roll
        self.dep=department
        print(self.name,self.age,self.place)
        print(self.roll,self.dep)
st=Student()
st.setper("aravind",22,"wayanad")
st.setstu(14,"Python")
