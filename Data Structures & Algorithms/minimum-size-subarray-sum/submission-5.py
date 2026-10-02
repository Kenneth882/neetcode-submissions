class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=float("inf")
        cur_total=0
        l=0
        for r in range(len(nums)):
            if nums[r]+cur_total>=target:
                res=min(res,r-l+1)
                cur_total+=nums[r]
                cur_total-=nums[l]
                l+=1
                while cur_total>=target:
                    res=min(res,r-l+1)
                    cur_total-=nums[l]
                    l+=1
            else:
                cur_total+=nums[r]
        
        
        if res==float("inf"):
            return 0
        else:
            return res