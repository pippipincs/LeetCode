# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        curr = root
        while queue:
            curr = queue.popleft()
            if curr.right:
                queue.append(curr.right)
            if curr.left:
                queue.append(curr.left)
        return curr.val