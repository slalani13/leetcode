# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxDepth = 0
        stack = [[root, 1]]

        while stack:
            for i in range(len(stack)):
                node, depth = stack.pop()
                maxDepth = max(maxDepth, depth)
                if node.left:
                    stack.append([node.left, depth+1])
                if node.right:
                    stack.append([node.right, depth+1])
        return maxDepth

