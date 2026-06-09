"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def proccess(child, prev, leftmost):
            if child:
                if prev == None:
                    prev = child
                    leftmost = child
                else:
                    prev.next = child
                    prev = child
            return prev, leftmost
                
        if root == None:
            return root
        leftmost = root
        while leftmost:
            curr = leftmost
            leftmost = None
            prev = None
            while curr:
                prev, leftmost = proccess(curr.left, prev, leftmost)
                prev, leftmost = proccess(curr.right, prev, leftmost)
                curr = curr.next
        return root