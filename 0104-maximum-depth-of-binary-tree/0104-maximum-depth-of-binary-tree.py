# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #recursive DFS
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # # BFS
        # if not root:
        #     return 0

        # #queue, set level, iterate through queue (current level), pop from queue, add neighbors
        # q = deque()
        # q.append(root)
        # level = 0

        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level += 1
        # return level

        # iterative DFS
        # use stack, add root node and depth, go through stack, add neighbors, 
        if not root:
            return 0
        stack=[[root, 1]]
        res = 0
        while stack:
            for i in range(len(stack)):
                node, depth = stack.pop()
                res = max(res, depth)
                if node.left:
                    stack.append([node.left, depth+1])
                if node.right:
                    stack.append([node.right, depth+1])
        return res