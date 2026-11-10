class Solution:
    def tribonacci(self, n: int) -> int:
        zero=0
        one=1
        two=1
        i=3
        if n<i:
            if n==0:
                return 0
            else:
                return 1
        while i<=n:
            prev2=two
            prev1=one
            two=two+one+zero
            one=prev2
            zero=prev1
            i+=1
        return two
        