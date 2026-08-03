class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        heap = []
        for element, freq in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, element))
            else:
                heapq.heappushpop(heap, (freq, element))
        return [element for freq, element in heap]