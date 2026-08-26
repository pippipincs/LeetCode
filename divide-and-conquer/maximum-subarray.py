class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = -math.inf
        presum = 0
        for num in nums:
            if presum < 0:
                presum = num
                maxsum = max(maxsum, presum)
            else:
                presum += num
                maxsum = max(maxsum, presum)
        return maxsum