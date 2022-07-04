#print those who are bigdata
lst=[[101,'amal','e',25,'bigdata',15000],
    [102,'vishnu','m',26,'python',15000],
    [103,'anoop','kp',25,'bigdata',15000],
    [104,'adarsh','s',28,'python',15000],
    [105,'ram','e',25,'bigdate',15000],
    [106,'aswin','k',30,'bigdata',15000]]

for i in lst:
    if(i[4]=='bigdata'):
        print(i[1:6])