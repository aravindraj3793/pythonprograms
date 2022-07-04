num=int(input("Enter Number")) #153
res=0
while(num!=0): #153!=0...15!=0
    dig=num%10 #153%10=3...15%10=5
    res=(res*10)+dig #(0*10)+3=3...(3*10)+5=35...
    num=num//10 #153//10=15....15//10=1
print(res)