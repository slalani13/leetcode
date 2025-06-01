# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # return true if there is a root to leaf path whose sum is targetSum
        # dfs to iterate through binary tree
        # base cases: if not root return false
        # if node is leaf node check currentSum and return true if equals target sum
        def helper(root, currentSum):
            if not root:
                return False
            currentSum += root.val
            if not root.left and not root.right: # leaf node
                if currentSum == targetSum:
                    return True
                return False
            if helper(root.left, currentSum):
                return True
            if helper(root.right, currentSum):
                return True
            return False
        return helper(root, 0)
        # since int is immutable, each currentSum is a new object
        # helper(root=5, sum=5) target = 22 -> True
        # helper(5.left = 4, sum=9) -> True
        # helper(4.left = 11, sum=20) -> True
        # helper(11.left = 7, sum=27) -> False
        # helper(11.right = 2, sum=22) -> True
            