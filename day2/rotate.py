def rotarry(nums,k):
   return nums[-k:]+nums[:-k]
nums=[1,2,3,4,5,6,7]
print(rotarry(nums,3))
