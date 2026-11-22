class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
      
        l=0
        r=len(arr)-1
        res=float("inf")
        while l<=r:
            middle=l+r
            if arr[middle]==middle:
                res=min(res,middle)
                r=middle-1
            elif arr[middle]<middle:
                l=middle+1
            else:
                r=middle-1
        if res==float("inf"):
            return -1
        else:
            return res
                
        
