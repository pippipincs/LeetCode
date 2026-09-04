class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = collections.Counter(nums)
        res = []
        def helper(perm, k):
            if k == len(nums):
                res.append(perm.copy())
                return
            for num in counter.keys():
                if counter[num] > 0:
                    perm.append(num)
                    counter[num] -= 1
                    helper(perm, k + 1)
                    counter[num] += 1
                    perm.pop()
        helper([], 0)
        return res
            