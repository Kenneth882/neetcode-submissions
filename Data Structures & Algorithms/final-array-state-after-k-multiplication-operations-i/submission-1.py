class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap=[]
        for i,v in enumerate(nums):
            heap.append([v,i])
        heapq.heapify(heap)
        i=0
        while i<k:
            curr=heap[0][0]
            curr_index=heap[0][1]
            res=curr*multiplier
            nums[curr_index]=res
            heapq.heappop(heap)
            heapq.heappush(heap,[res,curr_index])
            i+=1
        return nums



        
        