class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            #Trick is that one side is always sorted, goal is to find that side     
            middle=(l+r)//2
            if nums[middle]==target:
                return middle
            elif nums[l]<=nums[middle]:
                if nums[l]<=target<nums[middle]:
                    r=middle-1
                else:
                    l=middle+1
            elif nums[r]>nums[middle]:
                if nums[middle]<target<=nums[r]:
                    l=middle+1
                else:
                    r=middle-1
            
        return -1