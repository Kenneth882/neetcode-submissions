class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        store={}
        l=0
        for r in range(len(nums)):
            if nums[r] in store:
                return True
            if nums[r] not in store:
                store[nums[r]]=1
            if (r-l)+1>k:
                store.pop(nums[l])
                l+=1
        return False





