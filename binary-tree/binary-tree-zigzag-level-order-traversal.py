# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack1 = []
        stack2 = []
        res = []

        stack1.append(root)

        height = 0
        while stack1 or stack2:
            level = []
            if height % 2 == 0:
                while stack1:
                    node = stack1.pop()
                    level.append(node.val)
                    if node.left:
                        stack2.append(node.left)
                    if node.right:
                        stack2.append(node.right)
            if height % 2 == 1:
                while stack2:
                    node = stack2.pop()
                    level.append(node.val)
                    if node.right:
                        stack1.append(node.right)
                    if node.left:
                        stack1.append(node.left)
            res.append(level)
            height += 1
        return res