class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = 3
        N = 9
        sub_index = lambda r, c : (r // 3) * 3 + (c // 3)
        def next(row, col):
            if col == N - 1:
                backtrack(row + 1, 0, rows, cols, subs)
            else:
                backtrack(row, col + 1, rows, cols, subs)
        def backtrack(row, col, rows, cols, subs):
            if row == N:
                sudoku[0] = True
                return
            if board[row][col] != '.':
                next(row, col)
                return
            for d in range(1, 10):
                if d not in rows[row] and d not in cols[col] and d not in subs[sub_index(row, col)]:
                    rows[row].add(d)
                    cols[col].add(d)
                    subs[sub_index(row, col)].add(d)
                    board[row][col] = str(d)
                    next(row, col)
                    if sudoku[0]:
                        return
                    rows[row].remove(d)
                    cols[col].remove(d)
                    subs[sub_index(row, col)].remove(d)
                    board[row][col] = "."
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        subs = [set() for _ in range(N)]
        for r in range(N):
            for c in range(N):
                if board[r][c] != '.':
                    d = int(board[r][c])
                    rows[r].add(d)
                    cols[c].add(d)
                    subs[sub_index(r, c)].add(d)
        sudoku = [False]
        backtrack(0, 0, rows, cols, subs)

            