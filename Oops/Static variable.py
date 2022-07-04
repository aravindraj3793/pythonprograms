class Student:
    #here the variable college is same in all so we use static variable
    #static varibale given inside class
    college="abcd"
    def setvalue(self,name,rollno,dep):
        self.name=name
        self.rollno=rollno
        self.department=dep
    def printvalue(self):
        print(self.name)
        print(self.rollno)
        print(self.department)
        print(Student.college)
st1=Student()
st1.setvalue("Anu",5,"Science")
st1.printvalue()

st2=Student()
st2.setvalue("Ram",18,"Science")
st2.printvalue()

st3=Student()
st3.setvalue("manu",15,"commerce")
st3.printvalue()