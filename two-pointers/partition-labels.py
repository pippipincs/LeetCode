class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex = collections.defaultdict(int)
        for i, ch in enumerate(s):
            lastindex[ch] = i
        i = 0
        res = []
        while i < len(s):
            fartherest = lastindex[s[i]]
            j = i + 1
            while j <= fartherest:
                fartherest = max(fartherest, lastindex[s[j]])
                j += 1
            res.append(fartherest - i + 1)
            i = fartherest + 1
        return res
            