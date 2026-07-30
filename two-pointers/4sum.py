class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def two_sum(nums, target):
            res = []
            left, right = 0, len(nums) - 1
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    res.append([nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif s < target:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            return res
        def ksum(nums, target, k):
            res = []
            if k > len(nums):
                return res
            average = target // k
            if nums[0] > average  or nums[-1] < average:
                return res
            if k == 2:
                return two_sum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i - 1]:
                    for sub in ksum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + sub)
            return res
        nums.sort()
        return ksum(nums, target, 4)
