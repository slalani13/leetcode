class ListNode:
  
  def __init__(self, val, left_node = None, right_node = None) -> None:
    self.val = val
    self.prev = left_node
    self.next = right_node


class MyLinkedList:

  def __init__(self):
    self.head = ListNode(-1) 
    self.tail = ListNode(-1)
    self.head.next = self.tail
    self.tail.prev = self.head
    self.size = 0
     
  # get the value of the index
  def get(self, index: int) -> int:
    if index < 0 or index >= self.size:
      return -1
    
    curr = self.head.next
    while index > 0 and index < self.size:
      curr = curr.next
      index -= 1
    
    return curr.val
    
  def addAtHead(self, val: int) -> None:
    self.addAtIndex(0,val)

  def addAtTail(self, val: int) -> None:
    self.addAtIndex(self.size, val)

  def addAtIndex(self, index: int, val: int) -> None:
    if index < 0 or index > self.size:
        return None

    newNode = ListNode(val)
    curr = self.head.next

    while index > 0:
        curr = curr.next
        index -= 1

    newNode.next = curr
    newNode.prev = curr.prev

    curr.prev.next = newNode  # Update the next of the previous node
    curr.prev = newNode       # Update the previous of the current node

    self.size += 1

  def deleteAtIndex(self, index: int) -> None:
    if index < 0 or index >= self.size:
      return None
    
    curr = self.head.next
    while index > 0:
      curr = curr.next
      index -= 1
    
    curr.prev.next = curr.next
    curr.next.prev = curr.prev 

    self.size -=1
    


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)