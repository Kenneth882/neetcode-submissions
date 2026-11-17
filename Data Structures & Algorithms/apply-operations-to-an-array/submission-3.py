class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        l=0
        r=1
        n=len(nums)
        while r<len(nums):
            if nums[l]==nums[r]:
                nums[l]=nums[l]*2
                nums[r]=0
            l+=1
            r+=1
        
        l = 0
        r=0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums
                
                
        
