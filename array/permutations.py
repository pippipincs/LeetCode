class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        l = len(nums)
        def helper(perm, k):
            if k == l:
                res.append(perm.copy())
                return
            for num in nums:
                if num in perm:
                    continue
                perm.append(num)
                helper(perm, k + 1)
                perm.pop()
        helper([], 0)
        return res