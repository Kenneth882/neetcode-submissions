class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res=[]
        store={}
        count=0
        lencnt=0
        for i in range (len(grid)):
            for k in range(len(grid[i])):
                if grid[i][k] in store:
                    res.append(grid[i][k])
                    count+=1
                    lencnt+=count


                else:
                    store[grid[i][k]]=1
                    count+=1
                    lencnt+=count
        
        l=1
        while l<=count:
            if l in store:
                l+=1
                continue
            else:
                res.append(l)
                break
        return res
        