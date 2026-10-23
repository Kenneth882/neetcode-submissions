class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        count=0
        low=float("inf")
        for num in prices:
            if low>num:
                low=num
            elif low<num:
                curr=num-low
                count+=curr
                low=num
            else:
                continue 
        return count
        