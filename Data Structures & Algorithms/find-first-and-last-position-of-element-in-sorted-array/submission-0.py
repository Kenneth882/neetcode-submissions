class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        res=[]
        while l<=r:
            if nums[l]!=target:
                l+=1
            elif nums[r]!=target:
                r-=1
            else:
                res.append(l)
                res.append(r)
                return res
        res.append(-1)
        res.append(-1)
        return res


        