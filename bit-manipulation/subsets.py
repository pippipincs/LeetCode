class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(subset, curr):
            if curr == len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[curr])
            helper(subset, curr + 1)
            subset.pop()
            helper(subset, curr + 1)
        helper([], 0)
        return res