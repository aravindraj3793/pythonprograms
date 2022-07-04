#1.

for num in range(-2,-5,-1):
    print(num,end=" ")
#ans= -2,-3,-4

#2.

x=0
for i in range(10):
    for j in range(-1,-10,-1):
        x+=1
    print(x)
#ans=90

#3.

  for l in "john":
    if l=='o':
        break
    print(l,end=' ')
#ans=j
for l in "john":
    if l == 'o':
        pass
    print(l, end=' ')
#ans=j o h n

for l in "john":
    if l=='o':
        continue
    print(l,end=' ')
#ans=j h n

#4.

x=0
a=0
b=-5

 if(a>0):
     if(b<0):
         x=x+5
     elif(a>5):
         x=x+4
     else:
         x=x+3
 else:
     x=x+2
#ans=2

#5.
x=0
a=5
b=-5
if(a>0):
     if(b<0):
         x=x+5
     elif(a>5):
         x=x+4
     else:
         x=x+3
 else:
     x=x+2
#ans=5

#6.
a,b=12,5
if a+b:
    print("true")            #it will be true for every non zero number
else:
    print("false")
#ans=17  true

a,b=12,5
if a-b:
    print("true")            #it will be true for every non zero number
else:
    print("false")
#ans= -7  true

a,b=12,12
if a-b:
    print("true")            #it will be false for zero number
else:
    print("false")
#ans=0   false


