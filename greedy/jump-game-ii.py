class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[math.inf]*n
        dp[-1]=0
        for i in range(n-2,-1,-1):
            end=min(i+nums[i]+1,n)
            res=math.inf
            for j in range(i+1,end):
                res=min(dp[j]+1,res)
            dp[i]=res
        return dp[0]