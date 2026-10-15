class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        Find all elements that appear more than n>3
        if you have lets say len of 30/3 elements, there can only be at MAX 3 elements
        same with 60? yes each element can appear max 20 times
        maybe do three for loops
        to count and see if they are greater than n/3
        
        another approach i think could be having a hashmap and storing the value and counter then traversing through this getting the values that show up the most, i think this is the most intuative approach.

        """
        res={}
        great=[]
        n=len(nums)/3
        for num in nums:
            if num in res:
                res[num]+=1
            else:
                res[num]=1
        
        for key,value in res.items():
            if value>n:
                great.append(key)
            else:
                continue
        return great
