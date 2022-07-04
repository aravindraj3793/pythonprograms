#1,50
#even square
#odd cube

lst=[i**2 if i%2==0 else i**3 for i in range(1,51)]
print(lst)