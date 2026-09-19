class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=1
        while r<len(nums):
            if nums[l]==nums[r]:
                return nums[l]
            else:
                r+=1
                l+=1
        return nums[l]