class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        #make a max heap
        import heapq
        import math
        for i in range(len(gifts)):
            gifts[i]*=-1
        heapq.heapify(gifts)
        l=0
        while l<k:
            curr_max=gifts[0]*-1
            curr_max=math.floor(math.sqrt(curr_max))*-1
            heapq.heappop(gifts)
            heapq.heappush(gifts,curr_max)
            l+=1
        total=0
        for num in gifts:
            total+=(num*-1)
        return total

        
        