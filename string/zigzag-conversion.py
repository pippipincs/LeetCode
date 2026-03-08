class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zigzag = collections.defaultdict(list)
        i = 0
        change = 1
        for c in s:
            zigzag[i].append(c)
            if i == 0:
                change = 1
            elif i == numRows - 1:
                change = -1
            i += change
        res= ""
        for i in range(numRows):
            res += "".join(zigzag[i])
        return res
