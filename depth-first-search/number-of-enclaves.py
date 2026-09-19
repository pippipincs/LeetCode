class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(r, c):
            if grid[r][c] == 0:
                return
            grid[r][c] = 0
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                row = r + dr
                col = c + dc
                if row >= 0 and row < m and col >= 0 and col < n:
                    dfs(row, col)
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 1
        return res