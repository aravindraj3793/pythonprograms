f=open("numbers", "r")
list=[]
for i in f:
    if i not in list:
        list.append(int(i.rstrip("\n")))
print(list)
print(sum(list))
# to remove \n we use rstrip
#rstrip
#data=Var-name.rstrip("\n")



