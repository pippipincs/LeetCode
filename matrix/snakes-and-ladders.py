class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def getpos(num):
            num -= 1
            c = num // n
            if c % 2 == 0:
                col = num % n
            else:
                col = n - 1 - num % n
            row = n - 1 - c
            return row, col
        dq = deque()
        dq.append((1, 0))
        visited = set()
        visited.add(1)
        while dq:
            curr, steps = dq.popleft()
            if curr == n * n:
                return steps
            for nei in range(curr + 1, min(curr + 6, n * n) + 1):
                r, c = getpos(nei)
                if board[r][c] != -1:
                    nei = board[r][c]
                if nei not in visited:
                    dq.append((nei, steps + 1))
                    visited.add(nei)
        return -1
            