# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if not root or not p or not q:
        #     return None
        if root.val == p.val or root.val == q.val:
            return root
        elif root.val < q.val and root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > q.val and root.val > p.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
        
        
        