class Solution:
    def climbStairs(self, n: int) -> int:
        def reccursion_solution(n,cache):
            if n<=1:
                return 1
            elif n in cache:
                return cache[n]
            else:
                cache[n]=reccursion_solution(n-1,cache)+reccursion_solution(n-2,cache)
                return cache[n] # this will be the last value
                
        return  reccursion_solution(n,{})
    

        
        


