# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        val = [k]
        res = [None]
        def dfs(root, k):
            if not root:
                return 
            if res[0] is not None:
                return
            dfs(root.left, k)
            val[0] -= 1
            if val[0] == 0:
                res[0] = root.val
            dfs(root.right, k)

        dfs(root, k)
        return res[0]