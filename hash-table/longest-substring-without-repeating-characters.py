class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = -math.inf
        seen = set()
        l = 0
        for c in s:
            while c in seen:
                seen.remove(s[l])
                l += 1
            seen.add(c)
            res = max(res, len(seen))
        return res
