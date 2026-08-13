# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.compute_depth(root.left)
        right = self.compute_depth(root.right)

        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(left - right) <= 1
    def compute_depth(self, root):
        if not root:
            return 0
        left = self.compute_depth(root.left)
        right = self.compute_depth(root.right)
        return 1 + max(left, right)
    