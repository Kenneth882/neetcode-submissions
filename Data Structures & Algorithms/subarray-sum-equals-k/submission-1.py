class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map_count={0:1}
        count=0
        pre=0
        for num in nums:
            pre+=num
            if pre-k in map_count:
                count += map_count[pre-k]
                if pre in map_count:
                    map_count[pre]+=1
                else:
                    map_count[pre]=1
            

            else:
                if pre in map_count:
                    map_count[pre]+=1
                else:
                    map_count[pre]=1
        return count
        
            
            
        