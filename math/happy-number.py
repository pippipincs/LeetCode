class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            s = 0
            while n > 0:
                digit = n % 10
                n = n // 10
                s += digit * digit
            return s
        seen = set()
        seen.add(n)
        while True:
            n = get_next(n)
            if n == 1:
                return True
            if n in seen:
                return False
            else:
                seen.add(n)
        
            
