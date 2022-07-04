#Pattern 3
#1
#1 2
#1 2 3
#1 2 3 4

for i in range(1,5): #1...2.....
      for j in range(1,i+1): #(1,2)...(1,3)....
          print(j,end=' ') #1...1 2....
      print()