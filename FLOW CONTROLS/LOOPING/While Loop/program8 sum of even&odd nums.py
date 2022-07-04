low_lim=int(input("Enter lower limit"))
upp_lim=int(input("Enter upper limit"))
even_sum=0
odd_sum=0
i=low_lim
while(i<=upp_lim):
    if (i%2==0):
        even_sum+=i
    else:
      odd_sum+=i

    i+=1

print("Even sum",even_sum)
print("Odd sum",odd_sum)




