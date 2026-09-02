class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(s):
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        def helper(partition, index):
            if index == len(s):
                res.append(partition.copy())
                return
            for i in range(index, len(s)):
                p = s[index : i + 1]
                if not isPalindrome(p):
                    continue
                partition.append(p)
                helper(partition, i + 1)
                partition.pop()
        helper([], 0)
        return res
            