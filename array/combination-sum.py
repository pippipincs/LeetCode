class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(comb, curr):
            if sum(comb) > target:
                return 
            elif sum(comb) == target:
                res.append(comb.copy())
            for i in range(curr, len(candidates)):
                comb.append(candidates[i])
                helper(comb, i)
                comb.pop()
        helper([], 0)
        return res
