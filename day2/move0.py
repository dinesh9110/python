def movezeroes(nums):
    nums.sort(key=lambda x:x==0)
nums=[9,0,8,0,2,0]
movezeroes(nums)
print(nums)