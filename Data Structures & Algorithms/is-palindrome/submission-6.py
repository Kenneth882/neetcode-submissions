class Solution:
    def isPalindrome(self, s: str) -> bool:
       result = ''.join(filter(str.isalnum, s.lower()))

       l=0
       r=len(result)-1
       while l<r:
        if result[l]==result[r]:
            l+=1
            r-=1
        else:
            return False
       return True