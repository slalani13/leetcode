# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        # def inorder(root):
        #     if not root:
        #         return None
        #     inorder(root.left)
        #     res.append(root.val)
        #     inorder(root.right)
        # inorder(root)
        # return res

        # iterative solution uses a stack to trace the calls
        stack = [] # [1,5]
        curr = root # None
        res = [] # [4, 2, 6]
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            # curr is now None, pop from the stack for the most recent node added
            center_node = stack.pop() # 6
            res.append(center_node.val)
            curr = center_node.right     
        return res
        
        