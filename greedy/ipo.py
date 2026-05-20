import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minheap = []
        heapq.heapify(minheap)
        projects = sorted(list(zip(capital, profits)))
        length = len(projects)
        ptr = 0
        while ptr < length:
            if projects[ptr][0] <= w:
                heapq.heappush(minheap, -projects[ptr][1])
                ptr += 1
            else:
                break
        
        while k > 0 and minheap:
            
            w += -heapq.heappop(minheap)
            k -= 1
            while ptr < length:
                if projects[ptr][0] <= w:
                    heapq.heappush(minheap, -projects[ptr][1])
                    ptr += 1
                else:
                    break
        return w
