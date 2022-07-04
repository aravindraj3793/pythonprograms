lst=[2,3,1,10,15,13,14,12,11,4]
lst.sort()
print(lst)       #[1, 2, 3, 4, 10, 11, 12, 13, 14, 15]
low=0
flag=0
upp=len(lst)-1       #9
element=int(input("Enter your number")) #14
while(low<=upp):     #0<=9         5<=9         8<=9
    mid=low+upp//2   #(0+9)//2=4   (5+9)//2=7    (8+9)//2=8
    if(element>lst[mid]): #14>lst[4]  14>lst[7]  14>lst[8]
        low=mid+1    #4+1=5    7+1=8
    elif(element<lst[mid]): #14<14   condition not correct
        low=mid-1
    elif(element==lst[mid]): #14==14
        flag=1
        break
if(flag>0):
    print("Element found")
else:
    print("Not found")