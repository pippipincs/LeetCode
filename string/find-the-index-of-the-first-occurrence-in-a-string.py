class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        n = len(haystack)
        m = len(needle)

        if m > n :
            return -1
        ##find the lps of needle
        lps = [0] * m
        prev = 0
        i = 1
        while i < m :
            if needle[prev] == needle[i]:
                prev += 1
                lps[i] = prev
                i += 1
                continue
            elif prev == 0:
                lps[i] = 0
                i += 1
                continue
            else:
                prev = lps[prev - 1] 
                continue
        ## compare needle with haystack
        i = 0 # needle pointer
        j = 0 # haystack pointer
        while j < n:
            if haystack[j] == needle[i]:
                i += 1
                j += 1
                if i == m:
                    return j - m
            elif i != 0:
                i = lps[i - 1]
            else:
                i += 1
                j += 1
        return -1




            