class ListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyHashSet:

    def __init__(self):
        self.hashset = [ListNode(-1) for _ in range(1000)]

    def hash(self, key):
        return key % 1000

    def add(self, key: int) -> None: # O(n/1000)
        # find the index, check if the key exists, and then add key to linkedlist if it doesn't
        index = self.hash(key)
        cur = self.hashset[index]
        while cur.next:
            if cur.next.val == key: # if key already exists, return
                return
            cur = cur.next
        cur.next = ListNode(key) # else add key to linkedlist

    def remove(self, key: int) -> None:
        # find key in linkedlist under index and remove if exists
        index = self.hash(key)
        cur = self.hashset[index]
        while cur.next:
            if cur.next.val == key: # if key already exists, return
                cur.next = cur.next.next
                return
            cur = cur.next
        
    def contains(self, key: int) -> bool:
        # return true or false if key exists
        index = self.hash(key)
        cur = self.hashset[index]
        while cur.next:
            if cur.next.val == key: # if key already exists, return
                return True
            cur = cur.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)