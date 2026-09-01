class Solution:
    def findMin(self, nums: List[int]) -> int:
        res=float("inf")
        l=0
        r=len(nums)-1
        while l<r:
            middle=(l+r)//2
            res=min(res,nums[l],nums[r],nums[middle])
            if nums[r]<nums[middle]:
                l=middle+1
            if nums[r]>nums[middle]:
                r=middle-1
        if res==float("inf"):
            return nums[0]
        else:
            return res