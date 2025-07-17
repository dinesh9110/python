l=[-10,15,-20,30,-5,40]
pn=[x for x in l if x>=0]
print(pn)

l1=[1,3,5]
l2=[2,4,6]
c=[]
for i in range(len(l1)):
    for j in range(len(l2)):
        if i==j:
           c.append(l1[i])
           c.append(l2[j])
print(c)

n=[1,2,3,4,5,6,7,8,9]
te=n[2::3]
