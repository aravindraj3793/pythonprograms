#2nd largest
num1=int(input("Enter number1"))
num2=int(input("Enter number2"))
num3=int(input("Enter number3"))
if(num1>num2)&(num1>num3):
    if(num2>num3):
        print("2ND Largest number is",num2)
    else:
        print("2ND Largest number is",num3)
elif(num2>num1)&(num2>num3):
    if(num1>num3):
        print("2ND Largest number is",num1)
    else:
        print("2ND Largest number is",num3)
else:
    print("INVALID")