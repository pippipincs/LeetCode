class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        island_size = {}
        m = len(grid)
        n = len(grid[0])
        def dfs(r, c, mark):
            grid[r][c] = mark
            areas = []
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                row = r + dr
                col = c + dc
                
                if row >= 0 and row < m and col >= 0 and col < n:
                    if grid[row][col] == 1:
                        areas.append(dfs(row, col, mark))
            return 1 + sum(areas)
        mark = 2
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    island_size[mark] = dfs(i, j, mark)
                    mark += 1
        res = -math.inf
        if len(island_size) == 1 and m * n == island_size[2]:
            return m * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbours = set()
                    if i - 1 >= 0 and grid[i - 1][j] > 1:
                        neighbours.add(grid[i - 1][j])
                    if i + 1 < m and grid[i + 1][j] > 1:
                        neighbours.add(grid[i + 1][j])
                    if j - 1 >= 0 and grid[i][j - 1] > 1:
                        neighbours.add(grid[i][j - 1])
                    if j + 1 < n and grid[i][j + 1] > 1:
                        neighbours.add(grid[i][j + 1])
                    area = 1
                    for nei in neighbours:
                        area += island_size[nei]
                    res = max(res, area)
        return res

                    