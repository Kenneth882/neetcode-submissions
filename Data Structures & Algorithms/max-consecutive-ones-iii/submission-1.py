class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        zero_cnt=0
        res=0
        for r in range(len(nums)):
            if nums[r]==0:
                zero_cnt+=1
                if zero_cnt>k:
                    while zero_cnt>k:
                        if nums[l]==0:
                            zero_cnt-=1
                            l+=1
                        else:
                            l+=1
                
         
            res=max(r-l+1,res)
        return res
                    