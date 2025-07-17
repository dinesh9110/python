def reverse_string(s):
    s=list(s)
    reversed_s=""
    while s:
        reversed_s+=s.pop()
    return reversed_s
print(reverse_string("dinesh"))