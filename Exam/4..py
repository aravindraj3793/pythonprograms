#4. Print a pattern like

#  1
#  2 3
#  4 5 6
#  7 8 9 10
#  11 12 13 14 15

for i in range(1,6):
    for j in range(0,i+1,-1):
        print(i+j,end=" ")
    print()