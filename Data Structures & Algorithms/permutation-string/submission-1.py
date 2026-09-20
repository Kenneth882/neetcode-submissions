class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        curr={}
        key={}
        for s in s1:
            if s in key:
                key[s]+=1
            else:
                key[s]=1
        

        l=0
        
        length=len(s1)-1
        for r in range (len(s2)):
            if s2[r] in curr:
                curr[s2[r]]+=1
            else:
                curr[s2[r]]=1


            if r-l==length:
                if curr==key:
                    return True
                else:
                    #subtract the L value from the map if its 1 pop it if its not subtract by one
                    #Then increment l by one and append it to the hashmaphj
                    if curr[s2[l]]==1:
                        curr.pop(s2[l])
                        l+=1
                    else:
                        curr[s2[l]]-=1
                        l+=1
        return False                 
