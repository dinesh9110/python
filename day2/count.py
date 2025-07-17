n=int(input("enter a number"))
c=0
s=0
while n!=0:
    c+=1
    r=n%10
    s=s+r
    n//=10

print("digit count",c)
print("sum of digit",s)