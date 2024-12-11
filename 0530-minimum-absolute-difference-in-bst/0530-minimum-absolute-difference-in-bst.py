# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        arr = []
        def inorderTraversal(node):
            if not node:
                return

            inorderTraversal(node.left)
            arr.append(node.val)
            inorderTraversal(node.right)
    
        inorderTraversal(root)
        min_diff = float('inf')
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            min_diff = min(min_diff, diff)
        
        return min_diff