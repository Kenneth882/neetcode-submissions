# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,counter):
           
            
            if not node:
                 return False
            counter+=node.val
            if not node.left and not node.right:
                if counter==targetSum:
                    return True
                else:
                    return False
            
           
            return(dfs(node.left,counter) or 
            dfs(node.right,counter))





        return dfs(root,0)