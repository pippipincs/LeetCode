# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            node = TreeNode(val)
            return node
        if val < root.val:
            sub = self.insertIntoBST(root.left, val)
            root.left = sub
        else:
            sub = self.insertIntoBST(root.right, val)
            root.right = sub
        return root