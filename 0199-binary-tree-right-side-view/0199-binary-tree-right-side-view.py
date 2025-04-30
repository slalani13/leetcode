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
        q = deque()
        q.append(root)
        res = []
        while q:
            last_node = TreeNode(-1)
            for _ in range(len(q)):
                node = q.popleft()
                last_node = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(last_node.val)
        return res