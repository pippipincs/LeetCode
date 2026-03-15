class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums):
            target = 0 - nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[j] + nums[k]
                if s == target:
                    res .append([nums[i], nums[j], nums[k]])
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif s > target:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                else:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
        return res
                