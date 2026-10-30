class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        def back(num,curr,curr_sum):
            if num==len(nums) or curr_sum>target:
                return 
            if curr_sum==target:
                res.append(curr.copy())
                return
            
            curr.append(nums[num])
            curr_sum+=nums[num]
            
            back(num,curr,curr_sum)
            curr.pop()
            curr_sum-=nums[num]
            back(num+1,curr,curr_sum)
         
            



        back(0,[],0)
        return res



