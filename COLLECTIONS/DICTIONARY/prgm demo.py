dic={'name':'ram','age':22,'prof':'doctor','sal':100000}

#1.name====>fname
#2.print prof only
#3.check company is present in dic
#4.add a new keyand value company
#5.salary +5000
#6.print each key value pairs


#2.
print(dic['prof'])
#3.
print('company' in dic)
#4.
dic['company']='Aster'
print(dic)
#5.
dic['sal']+=5000
print(dic)
#6.
for i in dic:
    print(i,dic[i])