#list
#even num and odd num add to a sperate list
#print odd num sum and odd num sum



lst=[]
evn_lst=[]
odd_lst=[]
for i in range(1,76):
    lst.append(i)
print(lst)

for i in lst:
    if(i%2==0):
      evn_lst.append(i)

    else:
       odd_lst.append(i)

print('sum of list',sum(lst))
print('even_list sum',(sum(evn_lst)))
print('Odd_list sum',(sum(odd_lst)))