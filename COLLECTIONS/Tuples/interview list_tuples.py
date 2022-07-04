#Tuples cant change values
#here we need to change value of 20to100
tu=(10,15,20,25,30,35,40,45,50)

lst=list(tu)

lst[2]=100
print(lst)

tu=tuple(lst)
print(tu)