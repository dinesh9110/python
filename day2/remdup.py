def remdup(nums):
    i=0
    for j in range(1,len(nums)):
        if nums[i]!=nums[j]:
            i+=1
            nums[i]=nums[j]
    return i+1
nums=[1,1,2,3,3,3,3,4,10,11]
print(remdup(nums))