class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        prev=float("-inf")
        for i in range(len(arr)-1,-1,-1):
            if i+1==len(arr):
                prev=max(prev,arr[i])
                arr[i]=-1
            else:
                temp=arr[i]
                arr[i]=prev
                prev=max(prev,temp)
                 
        return arr           