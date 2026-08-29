class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        end, far = 0, 0
        for i in range(len(nums) - 1):
            far = max(far, i + nums[i])
            if i == end:
                res += 1
                end = far
        return res