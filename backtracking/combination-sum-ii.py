class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def helper(curr, comb):
            if sum(comb) == target:
                res.append(comb.copy())
                return
            elif sum(comb) > target:
                return
            for i in range(curr, len(candidates)):
                if i > curr and candidates[i] == candidates[i - 1]:
                    continue
                comb.append(candidates[i])
                helper(i + 1, comb)
                comb.pop()
        helper(0, [])
        return res