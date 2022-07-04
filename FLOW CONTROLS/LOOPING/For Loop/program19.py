#lower limit
#upper limit
#print prime numbers between lower and upper limit
low_lim=int(input("Enter lower limit"))
upper_limit=int(input("Enter upper limit"))
for num in range(low_lim,upper_limit+1):
    for i in range(2,num%i==0):
        break
    else:
        print(num)