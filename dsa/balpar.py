def is_balanced(expr):
    s=[]
    m={')':'(','}':'{',']':'['}
    for c in expr:
        if c in m:
            top=s.pop()
            if m[c]!=top:
                return False
        else:
            s.append(c)
    return not s
print(is_balanced("({[]})"))
print(is_balanced("({[)})"))