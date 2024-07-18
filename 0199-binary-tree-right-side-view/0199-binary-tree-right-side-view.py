# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        Q = deque()
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
            res.append(level[-1])
        return res