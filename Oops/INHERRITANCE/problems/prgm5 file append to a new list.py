class Emplyee:
    def __init__(self,id,fname,lname,age,profession,country):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.prof=profession
        self.country=country

    def printemp(self):
        print(self.id,self.fname,self.lname,self.age,self.prof,self.country)

list=[]
f=open("C:/Users/Lenovo/Downloads/customer","r")
for i in f:
    data=i.rstrip("\n").split(",")
    id=data[0]
    fname=data[1]
    lname=data[2]
    age=data[3]
    prof=data[4]
    country=data[-1]
    emp=Emplyee(id,fname,lname,age,prof,country)
    list.append(emp.id,emp.fname,emp.lname,emp.age,emp.prof,emp.country)
    print(list)