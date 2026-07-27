class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        i = 0
        minLen = math.inf
        for j in range(len(nums)):
            s += nums[j]
            if s < target:
                continue
            else:
                
                while s >= target and i <= j:
                    minLen = min(minLen, j - i + 1)
                    s -= nums[i]
                    i += 1
        return minLen if minLen != math.inf else 0
                
