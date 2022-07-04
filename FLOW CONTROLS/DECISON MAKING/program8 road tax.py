price=int(input("enter cost"))
tax=0
if(price>100000):
    tax=15/100*price
elif(price>50000 and price<=100000):
    tax=10/100*price
else:
    tax=5/100*price
print(tax)