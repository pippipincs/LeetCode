# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if nums == []:
            return None
        max_num = max(nums)
        i = nums.index(max_num)
        node = TreeNode(max_num)
        left = self.constructMaximumBinaryTree(nums[:i])
        right = self.constructMaximumBinaryTree(nums[i + 1 :])
        node.left = left
        node.right = right
        return node