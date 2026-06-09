# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder == []:
            return None
        v = postorder[-1]
        i = inorder.index(v)
        inorderleft = inorder[:i]
        inorderright = inorder[i+1:]
        postorderleft = postorder[:i]
        postorderright = postorder[i:-1]
        node = TreeNode(v)
        node.left = self.buildTree(inorderleft, postorderleft)
        node.right = self.buildTree(inorderright, postorderright)
        return node