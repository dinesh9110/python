def sort_stack(stack):
    temp_stack=[]
    while stack:
        temp=stack.pop()
        while temp_stack and temp_stack[-1]>temp:
            stack.append(temp_stack.pop())
        temp_stack.append(temp)
    return temp_stack
stack=[34,3,2,4,5,8,5,5]
print("Sorted stack:",sort_stack(stack))