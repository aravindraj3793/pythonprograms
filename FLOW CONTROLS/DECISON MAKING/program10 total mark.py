sub1=int(input("Enter mark of subject1"))
sub2=int(input("Enter mark of subject2"))
sub3=int(input("Enter mark of subject3"))
sub4=int(input("Enter mark of subject4"))
total=200
total_mark=sub1+sub2+sub3+sub4
if(total_mark>=180):
    print("A+")
elif(160<=total_mark<=179):
    print("A")
elif(140<=total_mark<=159):
    print("B+")
elif(120<=total_mark<=139):
    print("B")
elif(100<=total_mark<=119):
    print("C+")
elif(80<=total_mark<=99):
    print("C")
else:
    print("fail")