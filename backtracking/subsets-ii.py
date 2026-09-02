class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def helper(subset, curr):
            if curr == len(nums):
                res.append(subset.copy())
                return
            for i in range(curr, len(nums)):
                if i > curr and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                helper(subset, i + 1)
                subset.pop()
            helper(subset, len(nums))
        helper([], 0)
        return res