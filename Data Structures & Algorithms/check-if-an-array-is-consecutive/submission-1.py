class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        small=float("inf")
        big=float("-inf")
        res={}
        count=0
        for num in nums:
            small=min(small,num)
            big=max(big,num)
            count+=num
            if num in res:
                return False
            else:
                res[num]=1
        count2=0
        print(small)
        print(big)
        while small<=big:
            count2+=small
            small+=1
        
        print(count)
        print(count2)
        if count2==count:
            return True
        else:
            return False

