# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # use post order traversal and delete if leaf node
        # otherwise add it to stack
        # if already in stack, pop
        stack = [root]
        parents = {root: None} # root has no parent
        visited = set()
        while stack:
            node = stack.pop()
            if not node.left and not node.right and node.val == target:
                p = parents[node]
                if not p:
                    return None
                else:
                    if p.left == node:
                        p.left = None
                    else:
                        p.right = None
            elif node not in visited:
                visited.add(node)
                stack.append(node)
                if node.left:
                    stack.append(node.left)
                    parents[node.left] = node
                if node.right:
                    stack.append(node.right)
                    parents[node.right] = node
        return root
                

            
