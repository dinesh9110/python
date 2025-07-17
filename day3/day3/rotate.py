def rotate_right(l,k):
    k=k%len(l)
    return l[-k:]+l[:-k]
l=[1,2,3,4,6,7,8]
print(rotate_right(l,2))