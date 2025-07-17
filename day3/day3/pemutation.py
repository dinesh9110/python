from itertools import permutations
n=[1,2,3]
print(list(permutations(n)))
print(2 in n)
print(5 in n)

from collections import Counter
n=['dinesh',"jadi","dinesh","dinesh","nirmal","nirmal","tharun"]
f=Counter(n)
print(f)


n=[1,2,3,4,5,6,7]
m=len(n)//2
fhalf,shalf=n[:m],n[m:]
print(fhalf)
print(shalf)

l=[1,None,2,None,3,4,None]
f=[x for x in l if x !=None]
print(f)
cumsum=[sum(f[:i+1]) for i in range(len(f))]
print(cumsum)


char=['H','E','L','L','O']
print(''.join(char))

