# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        def dfs(node):
            if not node:
                return None
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        for i in range(len(res)):
            if i+1==k:
                return res[i]