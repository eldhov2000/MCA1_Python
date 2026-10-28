#-----------------7 A------------------


# list1=[1,2,4,3,8]
# list2=[1,2,4,3,5]
# print("The first list is:"+str(list1))
# print("The second list is:"+str(list2))
# l1=len(list1)
# l2=len(list2)
# print("lenght of list:",l1,"and length of list2:",l2)
# if l1==l2:
#     print("list are same length")
# else:
#     print("list are different length")
#

##---------------7 B--------------

list1=[1,2,4,3,8]
list2=[1,2,4,3,5]
print("The first list is:"+str(list1))
print("The second list is:"+str(list2))
sum1=0
sum2=0
for x in range(0,len(list1)):
    sum1=sum1+list1[x]
print("Sum of all elements in given list1:",sum1)
for x in range(0,len(list2)):
    sum2=sum2+list2[x]
print("Sum of all elements in given list2:",sum2)
if (sum1==sum2):
    print("list sum is to same value")
else:
    print("list sre of different sum")