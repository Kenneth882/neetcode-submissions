class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1={}
        hash2={}
        s1=list(s)
        s2=list(t)

        for i in s1:
            if i not in hash1:
                hash1[i]=1
            else:
                hash1[i]+=1
        for j in s2:
            if j not in hash2:
                hash2[j]=1
            else:
                hash2[j]+=1
        
        return hash1==hash2