class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if nums[0]%2==0:
            res=0
        else:
            res=1
        for i in range(1,len(nums)):
            curr=nums[i]%2
            if curr==res:
                return False
            else:
                res=curr
        return True