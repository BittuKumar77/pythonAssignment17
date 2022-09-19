# 6. Write a python program to add elements of list to a set
# thisset = {"Python", "Django", "JavaScript"}
# mylist = ["Java", "C"]

thisset={"python","Django","JavaScript"}
mylist={"java","C"}
thisset.update(mylist)
print(thisset)