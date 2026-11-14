# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.total=float("-inf")
        def dfs(node,path_value):
            if not node:
                return path_value
            left=dfs(node.left,path_value)
            right=dfs(node.right,path_value)
            path_value=max(node.val,node.val+left,node.val+right)
            self.total=max(self.total,node.val+right+left,path_value)
            return path_value
        dfs(root,float("-inf"))
        return self.total




        

        dfs(root,float("-inf"),float("-inf"))