f=open("C:/Users/Lenovo/Downloads/customer","r")
for i in f:
    data=i.rstrip("\n").split(",")
#age above 50 fname,lname,age,profession
    age=data[3]
    if(age>'50'):
        print(data[1:5])