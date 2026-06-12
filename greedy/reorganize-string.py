from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        heap = []
        heapq.heapify(heap)
        for char, nums in counts.items():

            heapq.heappush(heap, (-nums, char))
        cooldown = []
        i = 0 
        n = len(s)
        res = ""
        while i < n:
            for j in range(len(cooldown)):
                if cooldown[j][0] == 0:
                    _, nums, char = cooldown.pop(j)
                    heapq.heappush(heap, (nums, char))
                    break
            if heap:
                (nums, char) = heapq.heappop(heap)
                res += char
                nums += 1
            else:
                return ""
            
            for j in range(len(cooldown)):
                if cooldown[j][0] == 1:
                    cooldown[j][0] = 0
            if nums < 0:
                cooldown.append([1, nums, char])
            i += 1
        return res