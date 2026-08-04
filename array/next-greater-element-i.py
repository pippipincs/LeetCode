class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {}
        nums1_set = set(nums1)
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            num = nums2[i]
            while stack and stack[-1] <= num:
                stack.pop()
            
            if num in nums1_set:
                m[num] = stack[-1] if stack else -1
            stack.append(num)
        return [m[num] for num in nums1]
            