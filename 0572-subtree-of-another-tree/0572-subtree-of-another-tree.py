# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot))
        
        
    def isSameTree(self, nodeA, nodeB):
        if not nodeA and not nodeB:
            return True
        if not nodeA or not nodeB:
            return False
        if nodeA.val != nodeB.val:
            return False
        
        return self.isSameTree(nodeA.left, nodeB.left) and self.isSameTree(nodeA.right, nodeB.right)

