#1.create a list from element of a range from 1200 to 2000 with steps of 130
lst=[i for i in range(1200,2000,130)]
print(lst)

#2.lst=[44,54,64,74,104]
#    create a new list[40,50,60,70,100]
lst=[44,54,64,74,104]
lst2=[i+6 for i in lst]
print(lst2)

#3. create 1to15 elements [if element square >50 print it

lst3=[ i for i in range(1,16)  if(i**2>50)]
print(lst3)

#4.
dic={"sedan":1500,"Suv":2000,"pickup":2500,"minivan":1600,"van":2400,"semi":13600,"bicycle":200}
#print weight above 2000
#uppercase
lst4=[i.upper() for i in dic if(dic[i]>2000)]
print(lst4)