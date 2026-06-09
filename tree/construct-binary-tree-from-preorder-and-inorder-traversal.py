# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder == []:
            return None
        v = preorder[0]
        i = inorder.index(v)
        leftin = inorder[:i]
        rightin = inorder[i+1:]
        leftpre = preorder[1:1+i]
        rightpre = preorder[i+1:]
        node = TreeNode(v)
        node.left = self.buildTree(leftpre, leftin)
        node.right = self.buildTree(rightpre, rightin)
        return node