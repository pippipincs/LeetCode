class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        l = len(s)
        res = 0
        i = l - 1
        while i >= 0:
            if i == 0:
                res += values[s[i]]
                i -= 1
            elif values[s[i-1]] < values[s[i]]:
                res = res + values[s[i]] - values[s[i-1]]
                i -= 2
            else:
                res += values[s[i]] 
                i -= 1
        return res