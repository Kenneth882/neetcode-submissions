class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        pre=[0]*n
        suff=[0]*n
        suff[n-1]=1
        pre[0]=1

        #prefix
        for i in range (1,n):
            pre[i]=pre[i-1]*nums[i-1]
        #suffix
        for i in range(n-2,-1,-1):
            suff[i]= suff[i+1]*nums[i+1]
        #res
        for i in range(0,n):
            res[i]=pre[i]*suff[i]
        
        return res


        