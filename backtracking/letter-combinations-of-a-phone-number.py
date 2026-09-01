class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            2 : ['a', 'b', 'c'],
            3 : ['d', 'e', 'f'],
            4 : ['g', 'h', 'i'],
            5 : ['j', 'k', 'l'],
            6 : ['m', 'n', 'o'],
            7 : ['p', 'q', 'r', 's'],
            8 : ['t', 'u', 'v'],
            9 : ['w', 'x', 'y', 'z'],
        }
        res = []
        def helper(comb, index):
            if index == len(digits):
                res.append("".join(comb))
                return
            for ch in dic[int(digits[index])]:
                comb.append(ch)
                helper(comb, index + 1)
                comb.pop()
        helper([], 0)
        return res