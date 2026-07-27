class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        startrow = 0
        endrow = n - 1
        startcol = 0 
        endcol = n - 1
        k = 1
        res = [[0] * n for _ in range(n)]
        while k <= n * n:
            for c in range(startcol, endcol + 1):
                res[startrow][c] = k
                k += 1
            for r in range(startrow + 1, endrow + 1):
                res[r][endcol] = k
                k += 1
            for c in range(endcol - 1, startcol - 1, -1):
                res[endrow][c] = k
                k += 1
            for r in range(endrow - 1, startrow, -1):
                res[r][startcol] = k
                k += 1
            startrow += 1
            endrow -= 1
            startcol += 1
            endcol -= 1
        return res