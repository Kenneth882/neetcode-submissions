class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        #if two square numbers added=c
        square=[]
        l=0
        r=c
        while l<=r:
            middle=(l+r)//2
            if middle*middle==c:
                return True
            if middle*middle>c:
                r=middle-1
            else:
                while l<middle:
                    square.append(l*l)
                    l+=1
                square.append(middle*middle)
                l=middle+1
        l2=0
        r2=len(square)-1
        while l2<=r2:
            if square[l2]+square[r2]==c:
                return True
            if square[l2]+square[r2]>c:
                r2-=1
            else:
                l2+=1
        return False