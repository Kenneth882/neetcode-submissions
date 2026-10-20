class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        potential=None
        count=0
        for num in nums:
            if potential is None:
                potential=num
                count+=1
            elif potential!=num:
                if count==0:
                    potential=num
                    count+=1
                else:
                    count-=1
            if potential==num:
                count+=1
        return potential
                
