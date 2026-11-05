class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def back(curr,arr):
            if  len(arr)==k:
                res.append(arr.copy())
                return 
            if curr>n:
                return 
            arr.append(curr)
            back(curr+1,arr)
            arr.pop()
            back(curr+1,arr)


        back(1,[])
        return res