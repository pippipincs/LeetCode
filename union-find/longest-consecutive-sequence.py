class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        res = -math.inf
        for num in num_set:
            if num - 1 not in num_set:
                curr = num
                length = 1
                while curr + 1 in num_set:
                    curr = curr + 1
                    length += 1
                res = max(res, length)
        return res