cls_held=int(input("Enter Number of classes held"))
cls_attnd=int(input("Enter Number of classes Attended"))
percentage=(cls_attnd/cls_held*100)
print("Percentage=",percentage,"%")
if(percentage>75):
    print("Eligible for exam",)
else:
    print("Not eligible for exam")

