class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contains={}
        for i in nums:
            if i not in contains:
                contains[i]=1
            else:
                return True

        return False
    