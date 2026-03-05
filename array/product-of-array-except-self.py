class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(1, len(nums)):
            prefix *= nums[i - 1]
            res[i] = prefix
        suffix = 1
        for j in range(len(nums)-2, -1, -1):
            suffix *= nums[j + 1]
            res[j] *= suffix
        return res