dic={"roll":101,"name":'vinay',"age":22,"dep":'python',"marks":30}

#to change marks from 30to50
#dic["marks"]=50
#print(dic)

#or

dic["marks"]+=20
print(dic)

#to add a new keyword
dic["total"]=150
print(dic)

#to delete  keyword
del dic["roll"]
print(dic)