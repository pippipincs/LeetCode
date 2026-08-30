class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        collected = collections.defaultdict(int)
        for bill in bills:
            if bill == 5 or bill == 10:
                collected[bill] += 1
            if bill == 10:
                if collected[5] > 0:
                    collected[5] -= 1
                else:
                    return False
            if bill == 20:
                if collected[5] > 0 and collected[10] > 0:
                    collected[5] -= 1
                    collected[10] -= 1
                elif collected[5] >= 3:
                    collected[5] -= 3
                else:
                    return False
        return True