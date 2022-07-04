#create calculator
#1.Addition
#2.Substraction
#3.Multiplication
#4.Division

def add():
    num1=int(input("Enter Number1"))
    num2=int(input("Enter Number2"))
    sum=num1+num2
    print("ANSWER",sum)

def sub():
    num1 = int(input("Enter Number1"))
    num2 = int(input("Enter Number2"))
    subs=num1-num2
    print("ANSWER",subs)

def mul():
    num1 = int(input("Enter Number1"))
    num2 = int(input("Enter Number2"))
    multi=num1*num2
    print("ANSWER",multi)

def div():
    num1 = int(input("Enter Number1"))
    num2 = int(input("Enter Number2"))
    divi=num1/num2
    print("ANSWER",divi)

print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")

choice=int(input("Enter your choice"))
if(choice==1):

    add()
elif(choice==2):
    sub()

elif(choice==3):
    mul()
elif(choice==4):

    div()
else:
    print("INVALID")

