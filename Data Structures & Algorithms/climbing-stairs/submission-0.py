class Solution:
    def climbStairs(self, n: int) -> int:
        def reccursion_solution(n):
            if n<=1:
                return 1
            else:
                return reccursion_solution(n-1)+reccursion_solution(n-2)
        return  reccursion_solution(n)
    

        
        


