class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res1={}
        res2={}
        for char in s:
            if char in res1:
                res1[char]+=1
            else:
                res1[char]=1
        for char in t:
            if char in res2:
                res2[char]+=1
            else:
                res2[char]=1

        return res1==res2