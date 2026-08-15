# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        def helper(node, isleft):
            if not node.left and not node.right and isleft:
                res += node.val
                return
            if node.left:
                helper(node.left, True)
            if node.right:
                helper(node.right, False)
        helper(root, False)
        return res