class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:    
        from math import ceil  
        r=max(piles)
        l=1
        k=max(piles)
        while l<=r:
            temp=0
            middle=(l+r)//2
            
            for i in range(len(piles)):
                if middle>=piles[i]:
                    temp+=1
                    
                else:
                    temp+=math.ceil(piles[i]/middle)
                    
            if temp<=h:
                k=min(k,middle)
                r=middle-1
            else:
                l=middle+1
        return k