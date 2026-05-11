import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        l1 = len(nums1)
        l2 = len(nums2)
        
        pairs = []
        for i in range(l1):
            for j in range(l2):
                pairs.append([nums1[i] + nums2[j],nums1[i], nums2[j]])
        heapq.heapify(pairs)
        smallest = heapq.nsmallest(k, pairs)
        res = [[a, b] for s, a, b in smallest]
        return res