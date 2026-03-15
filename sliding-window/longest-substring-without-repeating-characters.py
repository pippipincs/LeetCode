class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        MaxLen = -math.inf
        left = 0
        visit = set()
        for right in range(len(s)):
            if s[right] not in visit:
                visit.add(s[right])
                MaxLen = max(MaxLen, len(visit))
            else:
                while s[right] in visit:
                    visit.remove(s[left])
                    left += 1
                visit.add(s[right])
                MaxLen = max(MaxLen, len(visit))
        return MaxLen   
