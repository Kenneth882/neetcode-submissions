class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res={0:1}
        pre=0
        count=0
        for num in nums:
            pre+=num
            if pre-k in res:
                count+=res[pre-k]
                if pre in res:
                    res[pre]+=1
                else:
                    res[pre]=1
            else:
                if pre in res:
                    res[pre]+=1
                else:
                    res[pre]=1
        return count
                


                