class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        MinLen = math.inf
        i = 0
        j = 0
        s = 0
        l = 0
        while j < len(nums):
            s += nums[j]
            l += 1
            while i <= j and s >= target:
                MinLen = min(MinLen, l)
                s -= nums[i]
                l -= 1
                i += 1
            j += 1
        return MinLen if MinLen != math.inf else 0
