class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        #two comaprison conditons 
        l=0
        r=len(nums)-1
        if nums[l]<=nums[r]:
            prev=0
            for i in range (1,len(nums)):
                if nums[i]<nums[prev]:
                    return False
                prev+=1
            return True 
        else:
            prev=0
            for i in range(1,len(nums)):
                if nums[prev]<nums[i]:
                    return False
                prev+=1
            return True

        
