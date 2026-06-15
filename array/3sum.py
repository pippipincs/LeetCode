class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        i = 0
        res = []
        while i < n:
            if nums[i] > 0:
                break
            first = nums[i]
            target = 0 - first
            l = i + 1
            r = len(nums) - 1
            while l < r :
                if nums[l] + nums[r] == target:
                    res.append([first, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                            l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
            i += 1
            while i < n and nums[i] == nums[i - 1]:
                i += 1
        return res