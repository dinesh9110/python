l=["zero","one","two","three","four","five","six","seven","eight","nine"]
n=int(input("enter a number"))
li=[]
while n!=0:
    r=n%10
    n=n//10
    li.extend([l[r]])
li.reverse()
print(','.join(li))