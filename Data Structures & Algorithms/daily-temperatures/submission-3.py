class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[]#would need to reverse later o(n) time
        for i in range(len(temperatures)-1,-1,-1):
            if not stack:
                res.append(0)
                stack.append([temperatures[i],i])
            elif temperatures[i]>=stack[-1][0]:
                while stack and temperatures[i]>=stack[-1][0]:
                    stack.pop()
                if not stack:
                    res.append(0)
                else:
                    res.append(stack[-1][1]-i)
                stack.append([temperatures[i],i])
            else:
                res.append(stack[-1][1]-i)
                stack.append([temperatures[i],i])
            
        l=0
        r=len(res)-1
        while l<=r:
            res[l],res[r]=res[r],res[l]
            l+=1
            r-=1
        return res
                
            


        