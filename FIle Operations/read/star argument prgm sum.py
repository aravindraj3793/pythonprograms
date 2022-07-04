def sum(*args):
    sum=0
    for i in args:
        sum+=i
        return sum
print(sum(10,20,10,40))
