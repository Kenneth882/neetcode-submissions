class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1=0
        count2=0
        res1=None
        res2=None

        for i in nums:
            if i==res1:
                count1+=1
            elif i==res2:
                count2+=1
            elif count1==0:
                count1=1
                res1=i
            elif count2==0:
                count2=1
                res2=i
            else:
                count1-=1
                count2-=1
        count1=0
        count2=0
        for num in nums:
            if res1== num:
                count1+=1
            elif res2 ==num:
                count2+=1
        res=[]
        if count1>len(nums)//3:
            res.append(res1)
        if count2>len(nums)//3:
            res.append(res2)
        return res







        