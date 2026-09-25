class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        L=0
        res=float("-inf")
        cur=0
        for R in nums:
            cur+=R
            
            res=max(cur,res)
            cur=max(cur,0)
        return res