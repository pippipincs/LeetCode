class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        j=n-1
        i=0
        while i<=j:
            if nums[i]!=val:
                i+=1
                continue
            else:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                j-=1
        return j+1
        