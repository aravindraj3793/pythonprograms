lst=[1,2,3,4,5,6,7,8,9,10]
#def even(num):
#   return num%2==0
#data=list(filter(even,lst))
#print(data)

#to reduce to single line:
data=list(filter(lambda num:num%2==0,lst))
print(data)
