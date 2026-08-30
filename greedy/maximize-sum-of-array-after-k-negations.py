class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        while i < len(nums):
            if nums[i] >= 0 or k == 0:
                break
            nums[i] = -nums[i]
            k -= 1
            i += 1
        if i < len(nums) and k % 2 == 1:
            nums[i] = -nums[i]
        return sum(nums)
        