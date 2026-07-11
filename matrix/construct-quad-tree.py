"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    
    def construct(self, grid: List[List[int]]) -> 'Node':
        self.grid = grid
        return self.solve(0, 0, len(self.grid))
        
    def same_Values(self, x, y, length):
        first = self.grid[x][y]
        for i in range(x, x + length):
            for j in range(y, y + length):
                if self.grid[i][j] != first:
                    return False
        return True
    def solve(self, x, y, length):
        if self.same_Values(x, y, length):
            return Node(self.grid[x][y], True)
        root = Node(False, False)
        half = length // 2
        root.topLeft = self.solve(x, y, half)
        root.topRight = self.solve(x, y + half, half)
        root.bottomLeft = self.solve(x + half, y, half)
        root.bottomRight = self.solve(x + half, y + half, half)
        return root
        
        


