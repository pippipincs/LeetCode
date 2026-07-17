class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        height = len(triangle)
        for h in range(1, height):
            row = triangle[h]
            last_row = triangle[h - 1]
            width = len(row)
            for i in range(width):
                if i == 0:
                    row[i] = last_row[0] + row[i]
                elif i == width - 1:
                    row[i] = last_row[-1] + row[i]
                else:
                    row[i] = min(last_row[i], last_row[i - 1]) + row[i]
        return min(triangle[-1])