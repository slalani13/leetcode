"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        h = {}
        cur = head
        
        while cur:
            copy = Node(cur.val)
            h[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            node = h[cur]
            node.next = h[cur.next] if cur.next else None
            node.random = h[cur.random] if cur.random else None
            cur = cur.next
        
        return h[head]