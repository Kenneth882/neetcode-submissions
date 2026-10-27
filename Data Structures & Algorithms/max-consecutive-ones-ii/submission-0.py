class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res=0
        l=0
        zero=0
        n=len(nums)-1
        for r in range(len(nums)):
            if nums[r]==0:
                zero+=1
                while zero>1:
                    if nums[l]==0:
                        zero-=1
                    l+=1
            res=max(r-l+1,res)      
        return res
                


