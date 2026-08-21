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
        node = TreeNode(v)
        i = inorder.index(v)
        left_in = inorder[:i]
        right_in = inorder[i + 1 :]
        len_left = len(left_in)
        len_right = len(right_in)
        left_post = postorder[:len_left]
        right_post = postorder[len_left:-1]
        left = self.buildTree(left_in, left_post)
        right = self.buildTree(right_in, right_post)
        node.left = left
        node.right = right
        return node