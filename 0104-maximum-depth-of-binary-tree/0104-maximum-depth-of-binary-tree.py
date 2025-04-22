# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = [0]

        def dfs(root, depth):
            if not root:
                return
            depth += 1
            max_depth[0] = max(depth, max_depth[0])
            dfs(root.left, depth)
            dfs(root.right, depth)
            return
        
        dfs(root, 0)
        
        return max_depth[0]
            
            
        