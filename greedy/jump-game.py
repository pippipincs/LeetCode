class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0] * len(nums)
        dp[-1] = 1
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, min((i + nums[i]+1), len(nums))):
                if dp[j] == 1:
                    dp[i] = 1
                    break
        return dp[0] == 1
        