class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(r, c):
            if grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for dr, dc in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                row = r + dr
                col = c + dc
                if row >= 0 and row < ROWS and col >= 0 and col < COLS:
                    dfs(row, col)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    cnt += 1
        return cnt