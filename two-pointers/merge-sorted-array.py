class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy=nums1[:m]
        i=0
        j=0
        p=0
        while p<(m+n):
            if i<m and j<n and nums1_copy[i]<nums2[j]:
                nums1[p]=nums1_copy[i]
                p+=1
                i+=1
            elif i<m and j<n and nums1_copy[i]>=nums2[j]:
                nums1[p]=nums2[j]
                p+=1
                j+=1
            elif i>=m:
                nums1[p]=nums2[j]
                p+=1
                j+=1
            elif j>=n:
                nums1[p]=nums1_copy[i]
                p+=1
                i+=1
            