names=["dinesh","tharun","jadi","nirmal"]
print(names.index("tharun"))
n=[1,2,3,4,5,6]
e=[x for x in n if x%2==0]
print(e)
u=[word.upper() for word in names]
print(u)
nest=[[1,2],[3,4],[5,6]]
flat=[num for sublist in nest for num in sublist]
print(flat)

def remdup(l):
    return list(set(l))
def maxi(l):
    return max(l)
def mini(l):
    return min(l)
def inter(l,b):
    return list(set(l)&set(b))
l=[1,1,2,2,3,3]
b=[3,334,3,4,5,6]
print(remdup(l))
print(maxi(l))
print(inter(l,b))
print(mini(l))

my_list=[]
if not my_list:
    print("list is empty")

n=[1,2,3,4]
s=1
for i in n:
    s=s*i
print(s)

people=[{'name':'alice','age':25},{'name':'bob','age':20}]
sorted_people=sorted(people,key=lambda x:x['age'])
print(sorted_people)


w=[' ','lovde','nirmal']
s=' '.join(w)
print(s)


def secmax(l):
    a=list(set(l))
    a.sort()
    return max([a[-2]])
l=[1,3,6,3,2,6]
print(secmax(l))

p=[('a',1),('b',2)]
print(dict(p))
