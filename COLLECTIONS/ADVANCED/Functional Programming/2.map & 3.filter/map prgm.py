#map
lst=[1,2,3,4,5,6,7,8,9,10]
#def square(num):
#    res=num**2
#    return res
#data=list(map(square,lst))
#print(data)

#to reduce to single line:
data=list(map(lambda num:num**2,lst))
print(data)