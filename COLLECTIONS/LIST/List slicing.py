lst=[10,52,64,32,89,74,22,34,62,55]

# List slicing

#positive index
#here it starts from 0 to end
#to print from 52to32
print(lst[1:4])

#to print from 32to62
print(lst[3:9])

#ex:
#1.
print(lst[:7]) #here lower limit starts from 0
#2.
print(lst[3:])#here it will print from 3to end of list
#3.
print(lst[:])#here it will print from 0 to end of list

#Negative index
#here it starts from -1 to -n
print(lst[-1])#55
print(lst[-3])#34
print(lst[-5])#74

print(lst[-4:-1]) #[22, 34, 62]
print(lst[-7:-3]) #[32, 89, 74, 22]
print(lst[-4:])
print(lst[-5:])



