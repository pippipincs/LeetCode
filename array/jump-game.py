class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        reach=[0]*len(nums)
        reach[0]=1
        for i in range(len(nums)):
            if reach[i]:
                for j in range(nums[i]):
                    if (i+1+j)<len(nums):
                        reach[i+1+j]=1
        return True if reach[-1] else False

