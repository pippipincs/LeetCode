class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prev = intervals[0][1]
        i = 1
        while i < len(intervals):
            interval = intervals[i]
            if interval[0] <= prev:
                prev = max(prev, interval[1])
                intervals[i - 1][1] = prev
                intervals.pop(i)
            else:
                prev = interval[1]
                i += 1
        return intervals