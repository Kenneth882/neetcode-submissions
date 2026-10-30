class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=0
        r=num
        while l<=r:
            middle=(l+r)//2
            curr=middle*middle
            if curr==num:
                return True
            else:
                if curr>num:
                    r=middle-1
                else:
                    l=middle+1
        return False