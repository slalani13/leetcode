# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if not root:
        #     return None
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root

        # BFS
        if not root:
            return None
        q = deque()
        q.append(root)

        while q:
            for i in range(len(q)):
                node = q.popleft()
                node.left, node.right =  node.right, node.left
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return root

        