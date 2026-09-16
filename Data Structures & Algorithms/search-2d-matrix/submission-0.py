class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        while l<=r:
            middle=(l+r)//2
            j=0
            k=len(matrix[middle])-1
            
            if matrix[middle][j]<=target<=matrix[middle][k]:
                while j<=k:
                    mid=(j+k)//2
                    if matrix[middle][mid]==target:
                        return True
                    elif matrix[middle][mid]>target:
                        k=mid-1
                    else:
                        j=mid+1
                return False
                
            elif target> matrix[middle][k]:
                l=middle+1
            else:
                r=middle-1
        return False





        