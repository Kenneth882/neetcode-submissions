class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n=len(skill)
        skill.sort()
        l=0
        r=n-1
        target=skill[l]+skill[r]
        count=0
        while l<r:
            if skill[r]+skill[l]==target:
                count+=skill[r]*skill[l]
                l+=1
                r-=1
                
            else:
                return -1
        return count