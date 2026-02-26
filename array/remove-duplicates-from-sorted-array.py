class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return 1
        i=0
        for j in range(size):
            if j == 0:
                nums[i] = nums[j]
                i += 1
            elif nums[j-1] != nums[j]:
                nums[i] = nums[j]
                i += 1
            else:
                continue
        return i
            