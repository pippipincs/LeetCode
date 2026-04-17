class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                val = board[i][j] 
                if val in rows[i]:
                    return False
                else:
                    rows[i].add(val)
                if val in cols[j]:
                    return False
                else:
                    cols[j].add(val)
                idx = (i // 3) * 3 + (j // 3)
                if val in boxes[idx]:
                    return False
                else:
                    boxes[idx].add(val)
        return True