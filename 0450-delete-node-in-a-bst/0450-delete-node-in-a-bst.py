# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # case 1 & 2: No children and one child
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                root.val = self.findMin(root.right)
                root.right = self.deleteNode(root.right, root.val)
        
        return root

    def findMin(self, node):
        if not node:
            return None
        
        if not node.left:
            return node.val
        else:
            return self.findMin(node.left)   

        