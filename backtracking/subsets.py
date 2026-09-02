class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res =[]
        def helper(subset, curr):
            if curr == len(nums):
                res.append(subset.copy())
                return
            for i in range(curr, len(nums)):
                subset.append(nums[i])
                helper(subset, i + 1)
                subset.pop()
            helper(subset, len(nums))
        helper([], 0)
        return res
        