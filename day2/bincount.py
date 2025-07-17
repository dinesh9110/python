n=int(input("enter a number"))
binary=bin(n)[2:]
print("binary:",binary)
l=list(binary)


print("binary:",binary)
print("zero count:",l.count('0'))
print("one count:",l.count('1'))
l.sort()
print(''.join(l))
