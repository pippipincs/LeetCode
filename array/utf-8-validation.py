class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        if len(data) > 4:
            return False