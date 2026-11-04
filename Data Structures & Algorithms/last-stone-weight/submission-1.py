class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]*=-1
        
        heapq.heapify(stones)
        while stones:
            if len(stones)==1:
                return stones[0] *-1
            if stones[0]==stones[1]:
                heapq.heappop(stones)
                heapq.heappop(stones)
            else:
                curr1=heapq.heappop(stones)
                curr2=heapq.heappop(stones)
                curr1*=-1
                curr2*=-1
                res=(curr1-curr2)*-1
                heapq.heappush(stones,res)
            


               
            
        return 0
                

        