class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = nums[0]
        res = -math.inf
        res = max(res, s)
        for n in nums[1:]:
            if s < 0:
                s = 0
            s += n
            res = max(res, s)
        return res
