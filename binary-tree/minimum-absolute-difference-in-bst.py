# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        res = math.inf
        def traverse(node):
            if not node:
                return
            nonlocal prev
            nonlocal res
            traverse(node.left)
            if prev is not None:
                res = min(res, abs(prev - node.val))
            prev = node.val
            traverse(node.right)
        traverse(root)
        return res
            