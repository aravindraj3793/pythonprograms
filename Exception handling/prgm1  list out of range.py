#lst=[5,6,7,4,3]
#print(lst[5])

#here it is list out of range error so we use try and except

lst=[5,6,7,4,3]
try:
    print(lst[5])
except:
    print("List out of range")