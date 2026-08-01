class Solution:
    
    def strStr(self, haystack: str, needle: str) -> int:
        occur=True
        for i in range(len(haystack)):
            for j in range(len(needle)):
                if i+j>=len(haystack) or needle[j]!=haystack[i+j]:
                    occur=False
                    break
            if occur:
                return i
            else:
                occur=True
        return -1