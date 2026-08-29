class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements={}
        for i in nums:
            if i not in elements:
                elements[i]=1
            else:
                elements[i]+=1
        initial=0
        for key,value in elements.items():
            if initial<value:
                initial=value
                final_key=key
        return final_key