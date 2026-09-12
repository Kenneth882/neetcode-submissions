class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        res={}
        out=[]
        
        for i, n in enumerate(nums):
            
            if target-n in res:
                out.append(res[target-n]) 
                out.append(i) 
                return out  
            res[n]=i
            
                