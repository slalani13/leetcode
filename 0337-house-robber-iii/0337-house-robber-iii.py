# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # subproblem: choose to take money from root, or money from left and right
        # recursive relation: rob(root) = max(rob(not_root), rob(root))
        # topology - linear iterate over tree
        # base case: no root: return (0, 0) not robbed amt, robbed amt
        # original problem: rob(root)
        # time comp: O(n)
        def dfs(root):
            if not root:
                return (0, 0) # did not rob, robbed
            
            left = dfs(root.left)
            right = dfs(root.right)

            # choose to rob node
            rob_node_amount = root.val + left[0] + right[0]
            # not rob node
            not_robbed = max(left) + max(right)

            return (not_robbed, rob_node_amount)
        
        return max(dfs(root))
        