class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l=0
        r=len(nums)-1
        while l<=r:
            middle=(l+r)//2
            if nums[middle]==target:
                return True
            elif nums[l]<nums[middle] or nums[r]>nums[l]:
                if nums[l]<=target<nums[middle]:
                    r=middle-1
                else:
                    l=middle+1

            
            elif nums[r]>nums[middle] or nums[l]>nums[r]:
                if nums[middle]<target<=nums[middle]:
                    l=middle+1
                else:
                    r=middle-1


            else:
                #cant tell which side is sorted, increment or decrement
                l+=1
            
            

        return False