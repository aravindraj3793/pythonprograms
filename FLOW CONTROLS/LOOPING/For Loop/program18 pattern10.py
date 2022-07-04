#0
#0 1
#0 2  4
#0 3  6 9
#0 4  8 12 16
#0 5 10 15 20 25
for i in range(0,6):
    for j in range(0,i+1):
        print(i*j,end=" ")
    print()