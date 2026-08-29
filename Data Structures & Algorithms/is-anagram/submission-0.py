class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hash_s={}
        hash_t={}
        for char1,char2 in zip(s,t):
            if char1 not in hash_s:
                hash_s[char1]=1
            elif char1 in hash_s:
                hash_s[char1]+=1
            if char2 not in hash_t:
                hash_t[char2]=1
            elif char2 in hash_t:
                hash_t[char2]+=1
        result=hash_s==hash_t
        return result

       
        
        