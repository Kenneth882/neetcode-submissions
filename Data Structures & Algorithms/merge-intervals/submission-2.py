class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        intervals.sort(key=lambda x:x[0])
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            if intervals[i][0]<=res[-1][1]:
                if intervals[i][1]>res[-1][1]:
                    res[-1][1]=intervals[i][1]
                else:
                    continue
            else:
                res.append(intervals[i])
        return res
        

        #logic u want to comapre ending point to next startting point.
        #i think u kind of also want to update the ending point as u go
        #for example u initially put the first interval value in the array,
        #if the next ending point is greater than the current ending point,
        #update this value, if it is not contiune, however the starting point must be less than the previous for this to happen. if none of the conditions above are true then just store next value and keep on going.
        