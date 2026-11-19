class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        init_min=min(arrays[0])
        init_max=max(arrays[0])
        res=0
        for i in range(1,len(arrays)):
            res=max(res,arrays[i][-1]-init_min,init_max-arrays[i][0])
            init_max=max(init_max,arrays[i][-1])
            init_min=min(init_min,arrays[i][0])
        return res

