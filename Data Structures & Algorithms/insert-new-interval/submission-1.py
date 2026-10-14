class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Look at starting times for the new interval and past interval
        " insert at new interval"
        O(N) traversal through this new array of intervals and then just do basic interval merging
        in the binary search part i think when middle is=target 
        """
        l=0
        r=len(intervals)-1
        target=newInterval[0]
        while l<=r:
            middle=(l+r)//2
            if intervals[middle][0]<target:
                l=middle+1
            else:
                r=middle-1
        intervals.insert(l,newInterval)
        res=[]
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            if intervals[i][0]>res[-1][1]:
                res.append(intervals[i])
            else:
                if intervals[i][1]>res[-1][1]:
                    res[-1][1]=intervals[i][1]
        return res

            
                