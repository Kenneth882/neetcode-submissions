class Solution:
    def climbStairs(self, n: int) -> int:
        curr=[1,1]#this works as the base case
        i=2
        while i<=n:
            tmp=curr[1]
            curr[1]=curr[0]+curr[1]
            curr[0]=tmp
            i+=1
        return curr[1]
    

        
        


