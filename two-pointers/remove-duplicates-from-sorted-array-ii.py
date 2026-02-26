class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1 or size == 2:
            return size
        count = 1
        i = 1
        
        while i < len(nums):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1
            if count > 2:
                nums.pop(i)
                count -= 1
                continue
            i += 1
        return len(nums)
