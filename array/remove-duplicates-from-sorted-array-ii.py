class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        if size ==1 or size ==2:
            return size
        i = 1
        count = 1
        j = 1
        while i < size:
            if nums[i] == nums[i-1]:
                count += 1
                if count > 2:
                    i += 1
                    continue
            else:
                count = 1
            nums[j] = nums[i]
            i += 1
            j += 1
        return j
