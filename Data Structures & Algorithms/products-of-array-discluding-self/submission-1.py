class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre=[0]*len(nums)
        suf=[0]*len(nums)
        res=[0]*len(nums)

        pre_res=1
        pre[0]=1
        
        for i in range(1, len(nums)):
            pre_res = nums[i-1] * pre_res   
            pre[i] = pre_res   
        suf_res=1             
        suf[-1]=1
        for j in range(len(nums)-1,-1,-1):
            suf[j]=suf_res
            suf_res=nums[j]*suf_res
        
        for k in range(len(nums)):
            res[k]=suf[k]*pre[k]
        return res
