class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(r, c):
            grid[r][c] = "0"
            for dr, dc in [[-1, 0], [0, 1], [0, -1], [1, 0]]:
                row, col = r + dr, c + dc
                if row >= 0 and row < m and col >= 0 and col < n and grid[row][col] == "1":
                    dfs(row, col)
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res
                   

