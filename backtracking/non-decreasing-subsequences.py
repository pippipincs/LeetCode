class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(last, sub, index):
            if index == len(nums):
                if len(sub) >= 2:
                    res.append(sub.copy())
                return
            exist = set()
            for i in range(index, len(nums)):
                d = nums[i]
                if d in exist:
                    continue
                if last == None:
                    exist.add(d)
                    sub.append(d)
                    backtrack(d, sub, i + 1)
                    sub.pop()
                else:
                    if d >= last:
                        exist.add(d)
                        sub.append(d)
                        backtrack(d, sub, i + 1)
                        sub.pop()
            backtrack(last, sub, len(nums))
        backtrack(None, [], 0)
        return res

