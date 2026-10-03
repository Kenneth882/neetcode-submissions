class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_res=float("inf")
        max_res=float("-inf")
        seen=set()
        for num in nums:
            if num<=0:
                continue
            else:
                min_res=min(min_res,num)
                max_res=max(max_res,num)
                seen.add(num)
        if min_res==float("inf") or min_res>1:
            return 1
        else:
        
            i=1
            while i<=max_res:
                if i not in seen:
                    return i
                else:
                    i+=1
            return i
