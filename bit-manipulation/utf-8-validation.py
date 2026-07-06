class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n_bytes = 0
        for  num in data:
            if n_bytes == 0:
                mask = 1 << 7
                n_bytes = 0
                while num & mask:
                    mask = mask >> 1
                    n_bytes += 1
                if n_bytes == 0:
                    continue
                        
                if n_bytes == 1 or n_bytes > 4:
                    return False
                
            else:
                mask1 = 1 << 7
                mask2 = 1 << 6
                if not (num & mask1 and not (num & mask2)):
                    return False
            n_bytes -= 1
        return n_bytes == 0