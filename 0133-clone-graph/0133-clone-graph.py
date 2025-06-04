"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # return a deep copy cloned node of the graph
        # use dfs to traverse the graph and return the cloned node
        # in each call, create a call and store it in a dict
        # dict = node : cloned_node
        # append its neighbors
        # O(n)

        
        hashmap = defaultdict(Node)
        def dfs(node):
            if not node:
                return None
            if node in hashmap:
                return hashmap[node]
            cloned_node = Node(node.val)
            hashmap[node] = cloned_node
            for nei in node.neighbors:
                cloned_neighbor = dfs(nei)
                cloned_node.neighbors.append(cloned_neighbor)
            return cloned_node
        return dfs(node)

            