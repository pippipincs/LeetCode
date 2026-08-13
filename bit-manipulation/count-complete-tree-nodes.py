# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compute_depth(self, root):
        d = 0
        while root.left:
            d += 1
            root = root.left
        return d
    def exist(self, idx, d, root):
        left = 0
        right = 2 ** d - 1
        for _ in range(d):
            mid = (left + right) // 2
            if idx <= mid:
                root = root.left
                right = mid
            else:
                root = root.right
                left = mid + 1
        return True if root else False
    

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        d = self.compute_depth(root)
        left, right = 0, 2 ** d - 1
        while left <= right:
            mid = (left + right) // 2
            if self.exist(mid, d, root):
                left = mid + 1
            else:
                right = mid - 1
        return 2 ** d - 1 + left