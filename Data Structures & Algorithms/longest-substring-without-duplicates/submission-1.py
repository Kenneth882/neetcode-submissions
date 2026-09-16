class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res={}
        count=0
        l=0
        for r in range(len(s)):
            while s[r] in res:
                res.pop(s[l])
                l+=1
            if s[r] not in res:
                res[s[r]]=1
            count=max(count,r-l+1)
        return count