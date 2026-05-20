import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minheap = []
        heapq.heapify(minheap)
        visited = set()
        for i, c in enumerate(capital):
                if i not in visited and c <= w:
                    heapq.heappush(minheap, -profits[i])
                    visited.add(i)
        while k > 0 and minheap:
            
            w += -heapq.heappop(minheap)
            k -= 1
            for i, c in enumerate(capital):
                if i not in visited and c <= w:
                    heapq.heappush(minheap, -profits[i])
                    visited.add(i)
        return w
