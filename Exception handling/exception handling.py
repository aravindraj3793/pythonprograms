#Exception Handling
#Errors that depend up on the input is called exceptional errors
#num1=int(input("Enter number1"))
#num2=int(input("Enter number2"))
#print(num1/num2)

#Exceptional handling
#3 blocks

#try      error
#except   solution
#finaly   

#ex:
num1=int(input("Enter number1"))
num2=int(input("Enter number2"))
try:
 print(num1/num2)
except:
 print("Zero division error")
finally:
 print("inside")