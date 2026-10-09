class Solution:
    def canJump(self, nums: List[int]) -> bool:
        total=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=total:
                total=i
            
        return total==0
            
