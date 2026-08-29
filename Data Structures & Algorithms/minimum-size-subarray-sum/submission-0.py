class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=float("inf")
        counter=0
        l=0
        for r in range(len(nums)):
            counter=counter+nums[r]
            while counter>=target:
                res=min(res,r-l+1)
                counter=counter-nums[l]
                l+=1
        if res==float("inf"):
            return 0
        else:
            return res
               