class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        

        def dfs(val,i,curr):
            if val==target:
                res.append(curr.copy())
                return 
            if i>= len(nums) or val>target:
                return None
            #here val has to be updated to add current i
            #curr must also be updated to take current values
            #i  should be updated once the current value is invalid
            curr.append(nums[i])
            dfs(val+nums[i],i,curr)
            curr.pop()
            dfs(val,i+1,curr)
        dfs(0,0,[])
        return res