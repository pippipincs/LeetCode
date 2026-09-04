class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def create_board(state):
            res = []
            for row in state:
                res.append("".join(row))
            return res
        ans = []
        def backtrack(rows, diag, anti, col, state):
            if col == n:
                board = create_board(state)
                ans.append(board)
                return
            for row in range(n):
                curr_diag = row - col
                curr_anti = row + col
                if (
                    row in rows
                    or curr_diag in diag
                    or curr_anti in anti
                ):
                    continue
                rows.add(row)
                diag.add(curr_diag)
                anti.add(curr_anti)
                state[row][col] = 'Q'

                backtrack(rows, diag, anti, col + 1, state)

                rows.remove(row)
                diag.remove(curr_diag)
                anti.remove(curr_anti)
                state[row][col] = '.'
        initial = [['.'] * n for _ in range(n)]
        backtrack(set(), set(), set(), 0, initial)
        return ans