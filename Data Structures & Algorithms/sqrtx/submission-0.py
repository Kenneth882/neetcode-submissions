class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=0,x
        res=0
        while l<=r:
            middle=(r+l)//2
            if middle*middle>x:
                r=middle-1
            elif middle*middle<x:
                l=middle+1
                res=middle
            else:
                return middle
        return res
        
                

