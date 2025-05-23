# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(root): # [1, 2]
            if not root:
                return None
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            if not root.left and not root.right:
                if root.val == target:
                    return None
            return root
        return dfs(root)