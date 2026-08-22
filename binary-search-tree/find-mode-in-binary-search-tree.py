# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        max_streak = 0
        curr_streak = 0
        curr_num = None
        ans = []
        def dfs(node):
            if not node:
                return
            nonlocal max_streak, curr_streak, curr_num, ans
            dfs(node.left)
            num = node.val
            if num == curr_num:
                curr_streak += 1
            else:
                curr_num = num
                curr_streak = 1
            if curr_streak > max_streak:
                ans = []
                ans.append(curr_num)
            elif curr_streak == max_streak:
                ans.append(curr_num)
            dfs(node.right)
        dfs(root)
        return ans