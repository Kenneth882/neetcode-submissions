class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        res=0
        cur=0

        while l<=r:
            cur=(r-l) * min(heights[l],heights[r])
            if cur>res:
                res=cur
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return res
            