class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes={}
        for i in nums:
            if i not in dupes:
                dupes[i]=1
            else:
                dupes[i]+=1
        new_dupes=dupes.values()
        for i in new_dupes:
            if i>1:
                return True
            else:
                pass
        return False


        