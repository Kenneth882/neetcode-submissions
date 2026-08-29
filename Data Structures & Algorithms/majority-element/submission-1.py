class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter=1
        res=nums[0]
        for i in range(1,len(nums)):
            if  res!= nums[i]:
                counter-=1
                if counter==0:
                    res=nums[i]
                    counter+=1
                else:
                    continue 
            elif res==nums[i]:
                counter+=1
        return res
            