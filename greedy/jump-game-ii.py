import math
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [math.inf] * len(nums)
        dp[-1] = 0
        for i in range(len(nums)-2,-1,-1):
            min_steps = math.inf
            for j in range(i+1, min((i + nums[i] + 1), len(nums))):
                if dp[j] < min_steps:
                    min_steps = dp[j]
            dp[i] = min_steps + 1
        return dp[0]