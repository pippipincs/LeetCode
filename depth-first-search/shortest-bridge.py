class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        def dfs(r, c):
            grid[r][c] = 2
            queue.append((r,c))
            for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                row = r + dr
                col = c + dc
                if row >= 0 and row < n and col >= 0 and col < n:
                    if grid[row][col] == 1:
                        dfs(row, col)
        found = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break
            if found:
                break
            
        
        
        distance = 0
        while queue:
            l = len(queue)
            for _ in range(l):
                r, c = queue.popleft()
                for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    row = r + dr
                    col = c + dc
                    if row >= 0 and row < n and col >= 0 and col < n:
                        if grid[row][col] == 1:
                            return distance
                        elif grid[row][col] == 0:
                            grid[row][col] = -1
                            queue.append((row, col))
            distance += 1
                       