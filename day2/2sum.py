#1.two sum problem
#find two numbers that add up to target
def twosum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return[i,j]
print(twosum([2,3,4,9,7],5))