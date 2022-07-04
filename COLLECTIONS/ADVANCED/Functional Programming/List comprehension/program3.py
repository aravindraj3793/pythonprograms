#(1,50)
#even square
#odd print itself
#(1,1),(2,4),(3,3).......

lst=[(i,i**2) if(i%2==0) else (i,i) for i in range(1,51)]
print(lst)