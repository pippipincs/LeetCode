class Solution:
    def longestPalindrome(self, s: str) -> str:
        L = len(s)
        def getpalin(i, j):
            while i >= 0 and j < L and s[i] == s[j]:
                i -= 1
                j += 1
            return j - i - 1
        maxl = 0
        start = 0
        for i in range(L):
            evenl = getpalin(i, i)
            oddl = getpalin(i, i + 1)

            currl = max(evenl, oddl)
            if currl > maxl:
                maxl = currl
                start = i - (maxl - 1) // 2
        return s[start : start + maxl]
