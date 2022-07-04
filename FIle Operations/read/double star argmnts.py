#**args

#def value(*args):
#    return args
#print(value(101,'Aravind','Raj',89456321,'wayanad'))


#we can add corresponding key or header to values in **args

def value(**args):
    return args

print(value(empno=101,fname='Aravind',lname='Raj',phno=89456321,place='wayanad'))

