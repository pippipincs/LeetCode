class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1:
            return 1
        length = 0
        i = len(s) - 1
        while i >=0:
            if s[i] == " " and length == 0:
                i -= 1
                continue
            if s[i] != " ":
                length += 1
                i -= 1
                continue
            if s[i] == " " and length > 0:
                return length
        return length