class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      result=set(nums)
      longest=0
      for i in nums:
        if (i-1) not in result:
            length=1
            while(i+length) in result:
                length+=1
            longest=max(longest,length)
      return longest
            