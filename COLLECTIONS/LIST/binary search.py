#Binary search
#algorithm
#    lst=[7,4,3,1,2]

#1. sort the list[ascending order]

 #lst=[1,2,3,4,7]

#2.Declare 2 variables
  #low=0
  #upp=len(lst)-1      :4

#3.calculate mid

  #mid=low+upp//2       0=4//2=2

#lst=[1,2,[3],4,7]
#lst[2]=3

#condition:
#1. searchelement>lst[mid]     4>3
     #low=mid+1

#2. searchelement<lst[mid]     2<3
     #low=mid-1

#3.searchelement==lst[mid]     3==3

