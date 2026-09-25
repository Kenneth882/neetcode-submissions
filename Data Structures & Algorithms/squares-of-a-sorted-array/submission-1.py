class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #Logic: The smallest and the largets values are stroed on the oppositie ends of the array. So example if -10 is the smallest and 100 is the largets then one is storeed at the strart and the othert is stored at the end. SO if wer initilize two pointers to the start and to the end then we are guarnteed to havbe the current bioggest squared value because as the array converges to the middle the values get smaller when squared.
        L=0
        R=len(nums)-1
        res=[]
        while L<=R:
            res1=nums[L]*nums[L]
            res2=nums[R]*nums[R]
            if res1>res2:
                
                res.append(res1)
                L+=1
            else:
                res.append(res2)
                R-=1
        #reverse
        L=0
        R=len(res)-1
        while L<=R:
            res[L],res[R]=res[R],res[L]
            L+=1
            R-=1
        return res