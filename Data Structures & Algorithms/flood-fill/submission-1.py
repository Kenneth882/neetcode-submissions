class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #The way i would solve this.
        """
        This problem is asking to start at index sr,sc and given that value, change every value it can reach to the color value.
        then at each value check if any neighbors have the same orignal value and then go there and change that value, once there is no orignal values, return 
        and the new image should be changed up
        """
        ref=image[sr][sc]
        if ref==color:
            return image
        def matrixdfs(r,c):
            rows=len(image)
            columns=len(image[0])
            if r==rows or columns==c:
                return 
            if image[r][c]!=ref:
                return 
            if min(r,c)<0:
                return 
            

            if image[r][c]==ref:
                image[r][c]=color
            matrixdfs(r+1,c)
            matrixdfs(r-1,c)
            matrixdfs(r,c+1)
            matrixdfs(r,c-1)            
            


                



        matrixdfs(sr,sc)
        return image