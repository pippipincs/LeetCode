class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            num = nums[i]
            while stack and stack[-1] <= num:
                stack.pop()
            res[i] = stack[-1] if stack else -1
            stack.append(num)
        for i in range(n - 1, -1, -1):
            num = nums[i]
            while stack and stack[-1] <= num:
                stack.pop()
            res[i] = stack[-1] if stack else -1
            stack.append(num)
        return res
        
        