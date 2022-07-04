student=('Anu',77),('vinay',55),('amal',35),('aswin',30)

marks=[]

for i in student:
    marks.append(i[1])


top_mark=max(marks)

for j in student:
    if(j[1]==top_mark):
     print(j[0],'has the Top mark')