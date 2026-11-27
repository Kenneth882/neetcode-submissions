class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
    #if water is ever touched, in this case 0, return 1, we do not want  to keep going on water tiles, just coming back, same with out of bounds, we do not want to keep going, just return 1, if we get to another brown spot then keep going, we want to prevent dupe visors, dupe visitors should return 0? yes because then they create an infinite loop and we do not want that.IN summery Out of bounds or water:return1, if its been visitied return 0, if its another land spot not visited keep going.  
        rows=len(grid)
        columns=len(grid[0])
        
        def dfs(r,c,visited):
            
            if (r,c) in visited:
                return 0 
            if (min(r,c)<0 or r==rows or c==columns or grid[r][c]==0):
                return 1
           
            

            visited.add((r,c))
            count=0
            #either up down left or right
            count+=dfs(r+1,c,visited)
            count+=dfs(r-1,c,visited)
            count+=dfs(r,c+1,visited)
            count+=dfs(r,c-1,visited)
            return count
        for r in range(rows):
                for c in range(columns):
                    if grid[r][c] == 1:
                        return dfs(r, c, set())
        


        