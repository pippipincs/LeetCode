class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest_reach=0
        n=len(nums)
        for i in range(n):
            if i>farthest_reach:
                return False
            farthest_reach=max(i+nums[i], farthest_reach)
            if farthest_reach>=n-1:
                return True

