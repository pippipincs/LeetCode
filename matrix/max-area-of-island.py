class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = -math.inf
        m = len(grid)
        n = len(grid[0])
        def dfs(r, c):
            nonlocal area
            if grid[r][c] == 0:
                return
            area += 1
            grid[r][c] = 0
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                row = r + dr
                col = c + dc
                if row >=0  and row < m and col >= 0 and col < n:
                    if grid[row][col] == 1:
                        dfs(row, col)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    area = 0
                    dfs(r, c)
                    maxArea = max(maxArea, area)
        return maxArea if maxArea != -math.inf else 0
