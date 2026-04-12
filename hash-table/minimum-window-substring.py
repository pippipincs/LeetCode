class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chars = Counter(t)
        ans = (math.inf, 0, 0)
        l,r = 0, 0
        found = collections.defaultdict(int)
        formed = 0
        required = len(chars)
        while r < len(s):
            c = s[r]
            found[c] += 1
            if c in chars and found[c] == chars[c]:
                formed += 1

            while l <= r and formed == required:
                ans = (min(ans[0], r - l + 1), l, r)
                c = s[l]
                found[c] -= 1
                if c in chars and found[c] < chars[c]:
                    formed -= 1
                l += 1


            r += 1
        return s[ans[1] :ans[2] + 1] if ans[0] != math.inf else ""

