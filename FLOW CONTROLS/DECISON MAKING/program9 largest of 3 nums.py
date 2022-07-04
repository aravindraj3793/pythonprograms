#largest among 3 numbers
num1=int(input("Enter number1"))
num2=int(input("Enter number2"))
num3=int(input("Enter number3"))
if(num1>num2)&(num1>num3):
    print("Largest number is",num1)
elif(num2>num1)&(num2>num3):
    print("Largest number is",num2)
else:
    print("Largest number is",num3)