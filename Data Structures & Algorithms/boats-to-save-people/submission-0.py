class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l=0
        r=len(people)-1
        people.sort()
        res=0
        while l<=r:
            if people[r]+people[l]>limit:
                res+=1
                r-=1
            elif people[r]+people[l]<=limit:
                res+=1
                l+=1
                r-=1
        return res
            