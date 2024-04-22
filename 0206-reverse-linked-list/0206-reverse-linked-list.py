# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #edge cases
        if not head:
            return None
        if not head.next:
            return head
        
        dummy = None
        prev = dummy
        curr = head
        next1 = curr.next

        while curr != None:
            curr.next = prev
            prev = curr
            curr = next1
            if next1:
                next1 = curr.next
        
        return prev