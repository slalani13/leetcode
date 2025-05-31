class ListNode:

    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr != self.tail:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def addAtHead(self, val: int) -> None:
        curr = self.head
        temp = curr.next
        curr.next = ListNode(val, temp, curr)
        temp.prev = curr.next
        self.length += 1

    def addAtTail(self, val: int) -> None:
        temp = self.tail.prev
        self.tail.prev = ListNode(val, self.tail, temp)
        temp.next = self.tail.prev
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # if index == length call add at tail. if index == 0, call add at head
        # if index > length return
        if index > self.length:
            return
        elif index == self.length:
            self.addAtTail(val)
            return
        elif index == 0:
            self.addAtHead(val)
            return
        curr = self.head # index 0
        i = 0
        while curr != self.tail: # curr points to node before new node
            if i == index:
                next_node = curr.next
                curr.next = ListNode(val, next_node, curr)
                next_node.prev = curr.next
                self.length += 1
                return
            i += 1
            curr = curr.next
        
    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index <= self.length-1: # valid index
            i = 0
            curr = self.head
            while curr != self.tail:
                if i == index:
                    temp = curr.next.next
                    curr.next = temp
                    temp.prev = curr
                    self.length -= 1
                    return
                i += 1
                curr = curr.next




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)