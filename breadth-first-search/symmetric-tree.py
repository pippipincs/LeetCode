# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric(left, right):
            if not left and not right:
                return True
            elif not left:
                return False
            elif not right:
                return False
            else:
                equal = left.val == right.val
                s1 = symmetric(left.left, right.right)
                s2 = symmetric(left.right, right.left)
                return equal and s1 and s2
        return symmetric(root.left, root.right)