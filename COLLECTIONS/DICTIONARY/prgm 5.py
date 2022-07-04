employee=['vinay','anu']
default={"designation":'Big Data',"Salary":10000}

#output want to be
#'vinay':{"designation":'Big Data',"Salary":10000},'anu':{"designation":'Big Data',"Salary":10000}
#here we use fromkeys
res=dict.fromkeys(employee,default)
print(res)

#if we want values of 1 specific key
print(res['vinay'])