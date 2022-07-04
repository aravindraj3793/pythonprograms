lst=[10,22,15,4,62,85,72,65]
num=int(input("Enter a number"))
flg=0
for i in lst:
    if(i==lst):
     flg=1
     break
if(flg>0):
     print("Element not found")
else:
    print("Element found")