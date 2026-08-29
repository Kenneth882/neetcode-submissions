class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            middle=(l+r)//2
            if nums[middle]==target:
                return middle
            elif nums[middle]>=nums[l]:
                if nums[middle]<target or target<nums[l]:
                    l=middle+1
                else:
                    r=middle-1
            elif nums[middle]<=nums[r]:
                if nums[middle]>target or nums[r]<target:
                    r= middle -1
                else:
                    l=middle +1
        return -1 