list1=["dinesh","jadi","nirmal","anil","suresh","varun"]
print(list1)
list1[1:3]=["ram"]
print(list1)

#append

list1.append("sham")
print(list1)
list1.insert(2,"vijay")
print(list1)
list1.extend(("nag","tharun","rahul"))
print(list1)
list1.remove("vijay")
print(list1)
list1.pop(3)
print(list1)
list1.sort()
print(list1)
list1.reverse()
print(list1)
print(list1.index("dinesh"))
print(list1.count("anil"))
list2=list1.copy()
print(list2)
list2.clear()
print(list2)
print(len(list1))
