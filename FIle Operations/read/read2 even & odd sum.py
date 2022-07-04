f=open("numbers", "r")
even_list=[]
odd_list=[]
list=[]

for i in f:
    if i not in list:
        list.append(int(i.rstrip("\n")))
print(list)
print("List sum",sum(list))
for i in list:
    if(i%2==0):
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)
print("Even sum",sum(even_list))
print("Odd sum",sum(odd_list))