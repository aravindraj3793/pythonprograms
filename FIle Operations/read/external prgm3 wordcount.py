f=open("C:/Users/Lenovo/Downloads/customer","r")
dic={}
for i in f:
    data=i.rstrip("\n").split(",")
#each prof count
    prof=data[4]
    if prof not in dic:
        dic[prof]=1
    else:
        dic[prof]+=1
print(dic)