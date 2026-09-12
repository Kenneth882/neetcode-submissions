class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0]!=0:
            return 0
        l=0
        r=1
        while r<len(nums):
            if nums[l]+1==nums[r]:
                l+=1
                r+=1
            else:
                return nums[r]-1
        return nums[r-1]+1
        
            
