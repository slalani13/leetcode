# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use fast and slow pointers to detect a cycle
        # if cycle use a third slow pointer and iterate until s2=s1, return slow
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if not fast or not fast.next:
            return None
        s2 = head
        s1 = slow
        while s1 != s2:
            s2 = s2.next
            s1 = s1.next
        return s2