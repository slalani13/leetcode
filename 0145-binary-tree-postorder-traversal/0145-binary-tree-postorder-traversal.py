# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if not root:
        #     return []
        res = []
        # stack = [(root, False)] # [1, 2, 4,  ]

        # while stack:
        #     node, visited = stack.pop()
        #     if node:
        #         if visited:
        #             res.append(node.val)
        #         else:
        #             stack.append((node, True))
        #             stack.append((node.right, False))
        #             stack.append((node.left, False))

        # return res
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
            return
        dfs(root)
        return res