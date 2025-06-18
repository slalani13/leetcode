# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # base case - if leaf node, return node.val, postorder traversal
        # max path sum options are - include current node + left node + right node if > 0
        maxSum = [float("-inf")]
        def dfs(root):
            if not root:
                return 0
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            maxSum[0] = max(maxSum[0], root.val + left + right) # path sum which includes current node
            return root.val + max(left, right)
        dfs(root)
        return maxSum[0]

        # dfs(root=-10), left = 9, right = 42, sum=42
        # dfs(root=9) -> 9
        # dfs(root=20), left = 15, right = 7 -> 42