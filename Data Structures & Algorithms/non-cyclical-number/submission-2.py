class Solution:
    def isHappy(self, n: int) -> bool:
        storage={}
        res=0
        while True:
            square=(n%10 * (n%10)) 
            res+=square
            n=n//10
            if n==0:
                if res==1:
                    return True
                else:
                    
                    if res in storage:
                        return False
                    storage[res]=1
                    
                    n=res
                    res=0
            
        