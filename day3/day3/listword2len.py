w=["dinesh","tharun","jadi","nirmal"]
c=["None" if x==2 else x for x in w]
print(c)

l=[1,2,2,3,4,4,5]
r=[]
for i in l:
    if l.count(i)<=1:
        r.append(i)
print(r)
