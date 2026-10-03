class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res={}
        l=0
        for r in range(len(nums)):
            if nums[r] in res:
                return True
            else:
                res[nums[r]]=1
            if (r-l)==k:
                res[nums[l]]-=1
                if res[nums[l]]==0:
                    res.pop(nums[l])
                    l+=1
                else:
                    l+=1
        return False             