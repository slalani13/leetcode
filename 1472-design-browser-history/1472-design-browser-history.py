# use a doubly linkedlist to move forward and backward
class DoublyNode:

    def __init__(self, url, prev=None, next=None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory: # [head -> leetcode -> google -> facebook -> youtube -> tail]

    def __init__(self, homepage: str): # O(1) # [head -> <- leetcode -> <- tail]
        self.head = DoublyNode(-1)
        self.tail = DoublyNode(-1)
        new_node = DoublyNode(homepage, self.head, self.tail)
        self.head.next = new_node
        self.tail.prev = new_node
        self.curr = new_node
        
    def visit(self, url: str) -> None:
        new_node = DoublyNode(url, self.curr, self.tail) # google, leetcode, tail
        self.curr.next = new_node # leetcode -> <-google -> <- tail
        self.tail.prev = new_node
        self.curr = new_node # google

    def back(self, steps: int) -> str: 
        # [head -> leetcode -> google -> facebook -> youtube -> tail]
        curr = self.curr
        for i in range(steps):
            if curr.prev == self.head:
                self.curr = curr
                return curr.url
            curr = curr.prev
        self.curr = curr
        return curr.url


    def forward(self, steps: int) -> str: #O(x)
        curr = self.curr
        for i in range(steps):
            if curr.next == self.tail:
                self.curr = curr
                return curr.url
            curr = curr.next
        self.curr = curr
        return curr.url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)