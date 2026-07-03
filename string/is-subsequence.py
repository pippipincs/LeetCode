class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1, p2 = 0, 0
        while p2 < len(t):
            if p1 == len(s):
                return True
            if t[p2] == s[p1]:
                p1 += 1
                p2 += 1
                continue
            p2 += 1
        return True if p1 == len(s) else False