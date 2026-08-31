class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[0])
        prevstart, prevend = points[0]
        arrows = 1
        for start, end in points[1:]:
            if start <= prevend:
                prevstart = start
            else:
                prevstart, prevend = start, end
                arrows += 1
        return arrows