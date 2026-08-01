class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # get the next array of needle
        next_needle = [0] * len(needle)
        j = -1
        next_needle[0] = j
        for i in range(1, len(needle)):
            while j >= 0 and needle[j + 1] != needle[i]:
                j = next_needle[j]
            if needle[j + 1] == needle[i]:
                j += 1
            next_needle[i] = j
        # search
        
        j = -1
        for i in range(len(haystack)):
            while j >= 0 and needle[j + 1] != haystack[i]:
                j = next_needle[j]
            if needle[j + 1] == haystack[i]:
                j += 1
            if j == len(needle) - 1:
                return i - len(needle) + 1
        return -1

        