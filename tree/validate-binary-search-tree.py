# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def findSmallest(root):
            smallest = root
            while smallest.left:
                smallest = smallest.left
            return smallest.val
        def findBiggest(root):
            biggest = root
            while biggest.right:
                biggest = biggest.right
            return biggest.val
        left, right = True, True
        if root.left:
            if findBiggest(root.left) >= root.val:
                return False
            left = self.isValidBST(root.left)
        if root.right:
            if findSmallest(root.right) <= root.val:
                return False
            right = self.isValidBST(root.right)
        if left and right :
            return True
        else:
            return False