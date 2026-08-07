class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] > heights[i]:
                curr = stack.pop()
                h = heights[curr]
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        while stack[-1] != -1:
            curr = stack.pop()
            h = heights[curr]
            w = len(heights) - stack[-1] - 1
            max_area = max(max_area, h * w)
        return max_area