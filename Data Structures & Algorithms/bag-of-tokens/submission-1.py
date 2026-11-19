class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score=0
        l=0
        r=len(tokens)-1
        res=0
        while l<=r:
            if power>=tokens[l]:
                score+=1
                power=power-tokens[l]
                res=max(res,score)
                l+=1
            else:
                #we need to look for power
                while power<tokens[l]:
                    if score<=0:
                        res=0
                        return res
                        break
                    else:
                        power+=tokens[r]
                        r-=1
                        score-=1
        return res
                    


