set = {1, 2, 3, 4, 5}
#set=[]
#set=int(input("Enter set Values"))
print(set)
e= int (input("enter number to remove"))
if e in set:
   remove=set.remove(e)
   print("Removed element:",remove)
   
else:
    raise KeyError("Set is empty")

print("Remaining set:",set)
