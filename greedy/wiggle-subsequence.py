class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        maxlen = 1
        sign = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] and sign != 1:
                maxlen += 1
                sign = 1
            elif nums[i] < nums[i - 1] and sign != -1:
                maxlen += 1
                sign = -1
        return maxlen
