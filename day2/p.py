# s=input()
# d=set(s)
# e=list(sorted(d))
# print(e)

def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)

# Example Usage
s1 = input().strip()
s2 = input().strip()

if is_rotation(s1, s2):
    print("Yes, it's a rotation")
else:
    print("No, not a rotation")
