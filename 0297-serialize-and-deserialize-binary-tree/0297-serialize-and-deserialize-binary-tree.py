# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # [1, 2, N, N, 3, 4, N, N, 5, N, N]
        data = []
        def dfs(root):
            if not root:
                data.append("N")
                return
            data.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        res = ",".join(data)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        self.i=0
        def dfs():
            if data[self.i] == "N":
                self.i += 1
                return None
            root = TreeNode(data[self.i])
            self.i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))