class Student:
    def setvalue(self,name,rollno,dep,college):
        self.name=name
        self.rollno=rollno
        self.department=dep
        self.college=college
    def printvalue(self):
        print(self.name)
        print(self.rollno)
        print(self.department)
        print(self.college)
st1=Student()
st1.setvalue("Anu",5,"Science","Don bosco")
st1.printvalue()

st2=Student()
st2.setvalue("Ram",18,"Science","rajagiri")
st2.printvalue()

st3=Student()
st3.setvalue("manu",15,"commerce","maharajas")
st3.printvalue()