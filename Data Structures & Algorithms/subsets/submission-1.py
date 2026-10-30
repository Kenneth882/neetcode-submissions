class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def back(num,curr):
            if num==len(nums):
                res.append(curr.copy())
                return 
            curr.append(nums[num])
            
            back(num+1,curr)
            curr.pop()
            back(num+1,curr)




        back(0,[])
        return res