#Set Operations

#1.Union
 #to combine 2 variables

st1={1,2,3,4,5}
st2={6,7,8,9,10}
st3=st1.union(st2)
print(st3)


#2.Intersection
#To collect common elemets in 2 variables

st4={1,2,3,4,5}
st5={5,6,7,8,9}
st6=st4.intersection(st5)
print(st6)


#3.Difference
#A-B  #element present in A and not in B

st1={1,2,3,4,5}
st2={5,6,7,8,9}
st3=st1.difference(st2)
print(st3)      #{1, 2, 3, 4}

#B-A  #element present in B and not in A

st1={1,2,3,4,5}
st2={5,6,7,8,9}
st3=st2.difference(st1)
print(st3)       #{8, 9, 6, 7}