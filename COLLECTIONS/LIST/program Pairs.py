lst=[4,5,10,15,20]
lst1=[]
total=sum(lst)   #51
for i in lst:    #4........5.....10....
    res=total-i   #51-4=47.....51-5=46....51-10=41....
    lst1.append(res)
print(lst)