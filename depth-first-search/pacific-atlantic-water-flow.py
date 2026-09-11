class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        def dfs(r, c, res, visited):
            res.append((r, c))
            visited.add((r, c))
            for dr, dc in [[1, 0], [-1, 0],[0, 1], [0, -1]]:
                row = r + dr
                col = c + dc
                if row >= 0 and row < m and col >= 0 and col < n:
                    if (row, col) not in visited and heights[row][col] >= heights[r][c]:
                        dfs(row, col, res, visited)
        pacific = []
        atlantic = []
        pacific_visited = set()
        atlantic_visited = set()
        for i in range(n):
            dfs(0, i, pacific, pacific_visited)
            dfs(m - 1, i, atlantic, atlantic_visited)
        for i in range(m):
            dfs(i, 0, pacific, pacific_visited)
            dfs(i, n - 1, atlantic, atlantic_visited)
        return list(set(pacific) & set(atlantic))
        