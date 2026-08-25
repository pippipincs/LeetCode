class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        j = 0
        res = 0
        for i in range(len(s)):
            if j >= len(g):
                break
            if s[i] >= g[j]:
                j += 1
                res += 1
        return res