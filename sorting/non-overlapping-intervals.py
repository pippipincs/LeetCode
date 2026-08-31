class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        prevstart, prevend = intervals[0][0], intervals[0][1]
        ans = 0
        for start, end in intervals[1:]:
            if start < prevend:
                ans += 1
                if end < prevend:
                    prevstart, prevend = start, end
                continue
            prevstart, prevend = start, end 
            
        return ans
            
