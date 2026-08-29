class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        findMin=float("inf")
        while l<=r:
            middle=(l+r)//2
            findMin=min(findMin,nums[middle])
            if nums[middle]>nums[r]:
                l=middle+1
            else:
                r=middle-1
        return min(findMin,nums[l])
