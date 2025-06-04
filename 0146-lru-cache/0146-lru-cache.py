class ListNode:
    def __init__(self, key=None, val=None, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.hashmap = {}  # key -> ListNode
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self._remove(node)
            self._add_to_tail(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            # Update value and move to MRU
            node = self.hashmap[key]
            node.val = value
            self._remove(node)
            self._add_to_tail(node)
        else:
            if self.size == self.capacity:
                # Evict LRU
                lru = self.head.next
                self._remove(lru)
                del self.hashmap[lru.key]
                self.size -= 1
            # Insert new node
            new_node = ListNode(key, value)
            self._add_to_tail(new_node)
            self.hashmap[key] = new_node
            self.size += 1

    def _remove(self, node: ListNode):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _add_to_tail(self, node: ListNode):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
