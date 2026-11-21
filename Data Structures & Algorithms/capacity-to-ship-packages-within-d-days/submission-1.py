class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total=0
        small=(float("-inf"))
        res=float("inf")
        for num in weights:
            total+=num
            small=max(small,num)
        l=small
        r=total
        
        while l<=r:
            middle=(l+r)//2
            i=0
            j=len(weights)-1
            curr=0
            capacity=0
            while i<=j:
                
                capacity+=weights[i]
                if capacity>middle:
                    capacity=0
                    curr+=1
                    i-=1
                
                if i==j:
                    curr+=1
                    break
                i+=1
           
            if curr<=days:
                res=min(res,middle)
                
                r=middle-1
            else:
                l=middle+1
        return res




                
                    

        

        


        