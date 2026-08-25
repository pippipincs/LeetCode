# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node, greater):
            if not node:
                return 0
            right = helper(node.right, greater)
            left = helper(node.left, node.val + right + greater)
            s = node.val + left + right
            node.val += greater + right
            return s
        helper(root, 0)
        return root