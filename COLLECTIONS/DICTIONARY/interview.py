#
lst=[1,3,5,6,8,9,6,4,3,2,5,8,9]
print(len(lst))
for i in range(0,len(lst)):
    if(lst[i-1]<lst[i]>lst[i+1])or(lst[i-1]>lst[i]<lst[i+1]):
        print(lst[i])
#2-6-22 video