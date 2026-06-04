class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        #first
        left, right = 0, len(nums) - 1
        while left <= right:
            mid  = (left + right) // 2
            if nums[mid] == target:
                if mid == 0 or (mid > 0 and nums[mid] > nums[mid - 1]):
                    res[0] = mid
                    break
                else:
                    right = mid - 1
            else:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        #last
        left, right = 0, len(nums) - 1
        while left <= right:
            mid  = (left + right) // 2
            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid] < nums[mid + 1]:
                    res[1] = mid
                    break
                else:
                    left = mid + 1
            else:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return res
        
         