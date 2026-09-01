class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def helper(comb, k, curr):
            if sum(comb) > n:
                return
            if 10 - curr < k:
                return
            if k == 0 and sum(comb) == n:
                res.append(comb.copy())
                return
            if k <= 0:
                return
            for num in range(curr, 10):
                comb.append(num)
                helper(comb, k - 1, num + 1)
                comb.pop()
        helper([], k, 1)
        return res
