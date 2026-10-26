class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        if nums[0]<0:
            j=1
            if nums[j]<0:
                while nums[j]<0:
                    nums[0],nums[j]=nums[j],nums[0]
                    j+=1
                nums[j],nums[0]=nums[0],nums[j]


            else:
                nums[j],nums[0]=nums[0],nums[j]
        for i in range(1,len(nums)):
            if nums[i]<0:
                if nums[i-1]>=0:
                    continue
                else:
                    j=i
                    while nums[j]<0:
                        nums[i],nums[j]=nums[j],nums[i]
                        j+=1
                    nums[j],nums[i]=nums[i],nums[j]
            else:
                if nums[i-1]<0:
                    continue
                else:
                    j=i
                    while nums[j]>=0:
                        nums[i],nums[j]=nums[j],nums[i]
                        j+=1
                    nums[j],nums[i]=nums[i],nums[j]
        return nums





