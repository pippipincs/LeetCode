class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        for i in range(k):
            prev = nums[-1]
            for j in range(n):
                nums[j], prev = prev, nums[j]
         