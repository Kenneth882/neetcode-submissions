class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        total=0
        heapq.heapify(sticks)
        while len(sticks)>1:
            curr1=heapq.heappop(sticks)
            curr2=heapq.heappop(sticks)
            res=curr1+curr2
            total+=res
            heapq.heappush(sticks,res)
        return total



