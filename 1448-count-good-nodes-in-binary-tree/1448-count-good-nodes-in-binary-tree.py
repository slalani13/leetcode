# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = [0]

        if not root:
            return 0
        def dfs(root, big):
            if not root:
                return 
            if root.val >= big:
                goodNodes[0] += 1
            big = max(root.val, big)
            dfs(root.left, big)
            dfs(root.right, big)
        dfs(root, root.val)
        return goodNodes[0]