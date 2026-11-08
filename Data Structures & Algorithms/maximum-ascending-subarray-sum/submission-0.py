class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res=0
        curr=0
        prev=0
        for i in range(len(nums)):
            if nums[i]>prev:
                curr+=nums[i]
                prev=nums[i]
            else:
                prev=nums[i]
                curr=nums[i]
            res=max(res,curr)
        return res
                