class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        def reverse(s):
            
            left, right = 0, len(s) - 1
            while left < right:
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left += 1
                right -= 1
            return s
        for i in range(0, len(s), 2*k):
            s[i : i + k] = reverse(s[i : i + k])
        return "".join(s)