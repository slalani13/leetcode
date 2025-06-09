# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        def reverse(head):
            if not head or not head.next:
                return head
            # let's say reverse returns the new_head of the linked_list
            new_head = reverse(head.next)
            head.next.next = head
            head.next = None
            return new_head

        # get to middle of linked list and reverse second half
        fast, slow = head, head
        # in even list, this goes to right side which is first node of second half
        # n is even
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse the linked list from slow
        second = reverse(slow)
        first = head
        maxTwinSum = 0
        while first and second:
            maxTwinSum = max(first.val + second.val, maxTwinSum)
            first = first.next
            second = second.next
        return maxTwinSum
        


        