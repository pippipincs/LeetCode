class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        prevstart, prevend = intervals[0][0], intervals[0][1]
        res = []
        for start, end in intervals[1:]:
            if start > prevend:
                res.append([prevstart, prevend])
                prevstart, prevend = start, end
            else:
                prevend = max(end, prevend)
        res.append([prevstart, prevend])
        return res