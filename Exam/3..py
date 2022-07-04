#3.python program to print prime number between 0 to 100
for num in range(0,100+1):
    if num>1:
        for i in range(2,num):
            if (num%i==0):
                break
        else:
            print(num)

