class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        res=[]
        for num in nums:
            curr=a*(num*num)+b*num+c
            res.append(curr)
        res.sort()
        return res