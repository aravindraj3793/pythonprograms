#* arguments

#def printval(num1,num2):
#    print(num1,num2)

#add(10,20)
#in here we add an extra value in print it will show error

#to overcome the drawback we use *args
#in *args we can assign more values

def add(*args):
    print(args) #if we use print(args) we can output in tuple format(10,20,10,25,45)

add(10,20,10,25,45)