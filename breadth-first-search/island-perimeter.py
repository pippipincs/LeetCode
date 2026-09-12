class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        peri = 0
        visited = set()
        m = len(grid)
        n = len(grid[0])
        def dfs(r, c):
            nonlocal peri
            visited.add((r, c))
            edges = 4
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                row = r + dr
                col = c + dc
                if row >= 0 and row < m and col >= 0 and col < n and grid[row][col] == 1:
                    edges -= 1
                    if (row, col) not in visited:
                        dfs(row, col)
            peri += edges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return peri
                    
            
        