class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res=[

        ]
        k=0
        
        for num in nums:
            if num==val:
                continue
            else:
                k+=1
                res.append(num)
        nums[:]=res

        return k
        