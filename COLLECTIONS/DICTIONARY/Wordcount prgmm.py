line='cat rat bus cat bus rat car cat car bat'

data=line.split(' ')

dic={}

for i in data:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1

print(dic)