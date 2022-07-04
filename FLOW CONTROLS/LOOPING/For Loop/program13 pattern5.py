#1 1 1 1 1
#2 2 2 2
#3 3 3
#4 4
#5


for i in range(1,6): #1..2
    for j in range(i,6): #(1,6) [j=1,j=2,j=3,j=4,j=5]...(2,6)...
        print(i,end=' ')#1 1 1 1 1....2 2 2 2
    print()