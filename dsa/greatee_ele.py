def nxt_greater_ele(arr):
    stack=[]
    result=[-1]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        while stack and stack[-1]<=arr[i]:
            stack.pop()
        if stack:
            result[i]