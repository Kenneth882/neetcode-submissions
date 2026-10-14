class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res=float("inf")
        l=0
        r=0
        while r<len(nums):
            if (r-l)==(k-1):
                curr=nums[r]-nums[l]
                res=min(res,curr)
                l+=1
                r+=1
            else:
                r+=1
            
        return res