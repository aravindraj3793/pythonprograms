#append
#to add elements to the list we can use append function
#append can only add single elements
lst=[]
lst.append(10)
lst.append(15)
lst.append(20)
lst.append('luminar')


#extend
#to add multiple elements we use extend
lst.extend([25,30,35])


#IN append and extend the elements only added in end postions


#insert
#to add elements only in to a particular position
#syntax
    #var_name.insert(index_value,element)
lst.insert(2,18)
print(lst)