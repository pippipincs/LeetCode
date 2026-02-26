class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        copy = nums[:]
        length = len(nums)
        i=0
        
        for j in range(len(copy)):
            if j == 0:
                nums[i] = copy[j]
                i+=1
                
            elif copy[j] != copy[j-1]:
                nums[i] = copy[j]
                i+=1
            else:
                continue
        return i