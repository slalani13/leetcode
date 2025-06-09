# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        def reverse(head):
            curr = head
            prev = None
            while curr:
                next = curr.next # save next
                curr.next = prev # reverse arrow
                prev = curr # update prev 
                curr = next # update curr
            return prev

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
        


        