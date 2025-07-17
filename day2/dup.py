def dup(l):
    for i in l:
        if l.count(i)>1:
            return True
            break
    return False
a=(1,2,3,3)
l=list(a)
print(dup(l))