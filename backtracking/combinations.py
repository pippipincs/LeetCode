class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(combine, k, curr):
            if k == 0:
                res.append(combine.copy())
                return
            for num in range(curr, n + 1):
                combine.append(num)
                helper(combine, k - 1, num + 1)
                combine.pop()
        helper([], k, 1)
        return res