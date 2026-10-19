class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        r=len(grid)
        c=len(grid[0])
        def matrixdfs(grid,r,c,store):
            row=len(grid)
            column=len(grid[0])
            if min(r,c)<0:
                return 0
            
            if (r,c) in store:
                return 0
            if r==row or c==column:
                return 0
            if grid[r][c]==1:
                return 0
            if r==row-1 and c==column-1:
                return 1
            store.add((r,c))

            count=0
            count+=matrixdfs(grid,r-1,c,store)
            count+=matrixdfs(grid,r+1,c,store)
            count+=matrixdfs(grid,r,c-1,store)
            count+=matrixdfs(grid,r,c+1,store)
            store.remove((r,c))
            return count

        return matrixdfs(grid,0,0,set())