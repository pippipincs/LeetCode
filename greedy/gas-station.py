class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        curr = 0
        start = 0
        i = 0
        while i < len(gas):
            total += gas[i] - cost[i]
            curr += gas[i] - cost[i]
            if curr < 0:
                curr = 0
                start = i + 1
            i += 1
        return start if total >= 0 else -1