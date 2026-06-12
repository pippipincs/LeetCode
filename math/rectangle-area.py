class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def overlapping(a1, a2, b1, b2):
            if b1 < a1:
                left = a1
            else:
                left = b1
            if b2 > a2:
                right = a2
            else:
                right = b2
            return right - left if right > left else 0
        width = overlapping(ax1, ax2, bx1, bx2)
        height = overlapping(ay1, ay2, by1, by2)
        return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - width * height