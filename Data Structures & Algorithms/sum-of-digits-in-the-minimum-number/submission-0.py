class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        res=float("inf")
        for num in nums:
            if num<res:
                res=num
        count=0
        while res>0:
            curr=res%10
            count+=curr
            res=res//10
        if count%2==0:
            return 1
        else:
            return 0
