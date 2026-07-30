class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums):
            num = nums[i]
            target = 0 - num
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                elif s > target:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                else:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
        return res
                
                