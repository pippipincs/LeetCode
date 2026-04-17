class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col = False
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j == 0:
                        col = True
                    else:
                        matrix[0][j] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for c in range(1, n):
                    matrix[i][c] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for r in range(1, m):
                    matrix[r][j] = 0
        if matrix[0][0] == 0:
            for c in range(1, n):
                matrix[0][c] = 0
        if col:
            for r in range(m):
                matrix[r][0] = 0
                