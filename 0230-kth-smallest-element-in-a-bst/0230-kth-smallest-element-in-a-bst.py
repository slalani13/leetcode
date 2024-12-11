# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order = []

        def inorderTraversal(node):
            if not node:
                return
            if len(order) == k:
                return
            inorderTraversal(node.left)
            order.append(node.val)
            inorderTraversal(node.right)

        inorderTraversal(root)
        return order[k-1]
        

