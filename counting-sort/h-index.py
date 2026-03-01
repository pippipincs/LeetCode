import math
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h_max = -math.inf
        for i in range(len(citations)-1, -1, -1):
            h = len(citations) - i
            if citations[i] >= h and h > h_max:
                h_max = h
            else:
                break
        return h_max