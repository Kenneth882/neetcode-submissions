class Solution:
    def mySqrt(self, x: int) -> int:
        #given integer x find the sqrt of it 
        l=0
        r=x

        while l<=r:
            middle=(l+r)//2
            if middle*middle==x:
                return middle
            elif middle*middle>x:
                r=middle-1
            else:
                l=middle+1
        return l-1