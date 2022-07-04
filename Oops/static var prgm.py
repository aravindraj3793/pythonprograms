class Student:
    institution_name="Luminar technolab"
    fees=29,500
    def setvalue(self,name,age):
        self.name=name
        self.age=age
    def printvalue(self):
         print(self.name)
         print(self.age)
         print(Student.institution_name)
         print(Student.fees)

st1=Student()
st1.setvalue("Aravind",22)
st1.printvalue()

st2=Student()
st2.setvalue("giffry",22)
st2.printvalue()


st1=Student()
st1.setvalue("manu",23)
st1.printvalue()




