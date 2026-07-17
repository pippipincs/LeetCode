class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                r1 = i - 1
                c1 = j
                r2 = i
                c2 = j - 1
                last_point = 0
                p1_exist = r1 >= 0 and r1 < m
                p2_exist = c2 >= 0 and c2 < n
                if p1_exist and p2_exist:
                    grid[i][j] += min(grid[r1][c1], grid[r2][c2]) 
                elif not p1_exist and p2_exist:
                    grid[i][j] += grid[r2][c2]
                elif not p2_exist and p1_exist:
                    grid[i][j] += grid[r1][c1]
                else:
                    continue
        return grid[m - 1][n - 1]
                