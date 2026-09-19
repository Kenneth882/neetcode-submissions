class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res={}
        for i in nums:
            if i in res:
                return i
            else:
                res[i]=1
        return 0