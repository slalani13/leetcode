# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        Q = deque()
        res = []
        Q.append(root)
        while Q:
            level = []
            for i in range(len(Q)):
                cur = Q.popleft()
                level.append(cur.val)
                if cur.left:
                    Q.append(cur.left)
                if cur.right:
                    Q.append(cur.right)
            res.append(level)
        return res