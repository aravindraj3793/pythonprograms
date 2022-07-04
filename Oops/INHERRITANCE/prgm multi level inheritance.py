#person(name,age)
#child(place,school)
#student(roll,dep,college)

class Person:
    def setper(self,name,age):
        self.name=name
        self.age=age

class Child(Person):
    def setchild(self,place,school):
        self.place=place
        self.school=school

class Student(Child):
    def setstu(self,rollno,department,college):
        self.rollno=rollno
        self.dep=department
        self.col=college
        print(self.name,self.age,self.place,self.school,self.rollno,self.dep,self.col)

st=Student()
st.setper("Aravind",22)
st.setchild("Wayanad","Nss")
st.setstu(17,"compuer_science","DONBOSCO")
