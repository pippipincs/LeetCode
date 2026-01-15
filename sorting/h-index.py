class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n=len(citations)
        for i,v in enumerate(citations):
            if n-i <= v:
                return n-i
        return 0

