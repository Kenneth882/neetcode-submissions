class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        #take prefix
        #take suffix
        #find max of each suff/pre array index
        #return the max one
        prefix=[]
        suffix=[0]*len(nums)
        pre=0
        suff=0
        for num in nums:
            pre+=num
            prefix.append(pre)
        for i in range(len(nums)-1,-1,-1):
            suff+=nums[i]
            suffix[i]=suff
        total=float("-inf")
        for i in range(len(prefix)):
            total=max(total,suffix[i],prefix[i])
        return total
        

