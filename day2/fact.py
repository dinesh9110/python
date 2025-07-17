def fact(x):
    if x==0 or x==1:
        return 1
    else:
        return x*fact(x-1)
n=int(input("enter a number"))
f=0
while n>0:
    c=fact(n)
    f=f+c
    n=n-1
print("fact=",f)