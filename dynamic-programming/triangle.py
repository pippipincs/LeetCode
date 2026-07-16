class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        height = len(triangle)
        dp = [[triangle[0][0]]]
        last_width = 1
        for h in range(1, height):
            width = len(triangle[h])
            dprow = []
            for i in range(width):
                v = triangle[h][i]
                s = math.inf
                for index in [i, i - 1]:
                    if index >= 0 and index < last_width:
                        s = min(dp[-1][index], s)
                dprow.append(s + v)
            dp.append(dprow)
            last_width = len(dprow)

        return min(dp[-1])


