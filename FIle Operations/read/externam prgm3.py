f=open("C:/Users/Lenovo/Downloads/customer","r")
for i in f:
    data=i.rstrip("\n").split(",")
#age above 50 & india fname,lname,age,profession
    age=data[3]
    country=data[-1]
    if(age>'50')&(country=='india'):
        print(data[1:5])