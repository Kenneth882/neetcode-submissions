class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        hash1={}
        hash2={}
        res=[]
        for num in arr1:
            hash1[num]=1
        for num in arr2:
            if num in hash1:
                hash2[num]=1
        for num in arr3:
            if num in hash2:
                res.append(num)
        return res
