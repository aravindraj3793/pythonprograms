f=open("contents","r")
dic={}
sp="!@#$%^&*()<>?"
for i in f:
    data=i.rstrip("\n")
    string=""
    for j in data:
        if j not in sp:
            string+=j
    print(string)

