# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(root):
            if root == None:
                return None
            if root.left == None and root.right == None:
                return root
            leftlist = helper(root.left)
            rightlist = helper(root.right)
            if leftlist:
                leftlist.right = root.right
                root.right = root.left
                root.left = None
            return rightlist if rightlist else leftlist
        helper(root)
        