class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr.sort()
        count=0
        for num in arr:
            if num + 1 in arr:
                count+=1
            else:
                continue
        return count