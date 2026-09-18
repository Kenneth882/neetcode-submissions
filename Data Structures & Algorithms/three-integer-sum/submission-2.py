class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       #what i know is needded.
       #No dupe values so eveything must be distinct
       #They must all add up to zero

        #this can be dne by itteratinmg then if current element is equal to the last just skip that as well
        # t prevent duplicate values.
        #Have one for loop that itterates through all values then another that itteates for all sub values
        #we can sort to ensure that we skip values previoiusly
        #Also we know that if the least value is greater than zero then stop because no values greater than -0 added can be equAL TO zero
        
        nums.sort()
        res=[]
        for i in range (len(nums)):
            if nums[i]>0:
                break
            if  i>0 and nums[i]==nums[i-1] :
                    continue

            l=1+i
            r=len(nums)-1
            
                

                      
            #what ishe stopping case for the inside loop?
            #SInce its sorted maybe use a 2 pointer metheod.
            while l<r:
                
                if nums[i]+nums[l]+nums[r]==0:
                    res.append([nums[i],nums[l],nums[r]])
                    #if its equal to zero now what??
                    r-=1
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                    
                     
                elif nums[i]+nums[l]+nums[r]<0:
                    l+=1
                else:
                    r-=1
        
        
        return res                
                
                    