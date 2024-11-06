# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]

        def height(node):
            if not node:
                return 0
            
            left = height(node.left)
            right = height(node.right)
            d = left + right
            diameter[0] = max(d, diameter[0])
            return max(left, right) + 1

        height(root)
        return diameter[0]