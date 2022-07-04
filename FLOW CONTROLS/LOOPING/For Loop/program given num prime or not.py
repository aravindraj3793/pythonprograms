#Check Given number is prime or not
num=int(input("Enter a number"))
flg=0
for i in range(2,num):
    if (num%i==0):
        flg=1
        break
if(flg>0):
      print(num,"is not a prime number")
else:
      print(num,"is a prime number")


