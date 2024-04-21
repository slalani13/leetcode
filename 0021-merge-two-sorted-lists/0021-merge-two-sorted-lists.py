# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # check edge cases
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        # choose initial head, advance ptr
        if list1.val < list2.val or list1.val == list2.val:
            curr = list1
            list1=list1.next
        else:
            curr = list2
            list2 = list2.next
        
        temp_head = curr
        while curr != None:
            if (list1 == None and list2 != None) or ((list1 and list2) and list1.val > list2.val):
                curr.next = list2
                list2 = list2.next
                curr = curr.next
                continue
            elif (list1 == None and list2 != None) or ((list1 and list2) and list1.val < list2.val):
                curr.next = list1
                list1 = list1.next
                curr = curr.next
                continue
            else:
                curr.next = list1
                if list1 != None:
                    list1 = list1.next
                curr = curr.next
        return temp_head

