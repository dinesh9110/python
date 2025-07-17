l=[1,2,3,4,5,6,7,8]
print(max(l)-min(l))

l=[1,2,3,4,5]
l[0],l[-1]=l[-1],l[0]
print(l)

l=[1,2,3,4,5]
f=[l[i] for i in range(len(l)) if i%2!=0]
print(f)