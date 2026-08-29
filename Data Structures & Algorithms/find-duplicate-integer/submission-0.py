class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_set={}
        for i in nums:
            if i in hash_set:
                return i
            else:
                hash_set[i]=1