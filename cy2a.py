from future.types import newlist

mylist=[23,58,-12,90,-40,81,49,-36]
print("First List:",mylist)
newlist=[x for x in mylist if x>0]
print("New List:",newlist)