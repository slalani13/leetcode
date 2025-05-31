# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 3 linkedlists merge and return in sorted order, each linked-list is already sorted
        # choose minimum between k lists, use heap and add k elements to min heap klogn
        # create dummy node and return dummy.next as head
        # pop node from heap, each node will have a next val, add next node to heap logn
        # connect node to curr node and update curr
        # Time complexity - n log n because we are gonna add all n nodes to heap eventually and stop when heap is empty
        minHeap = []
        heapq.heapify(minHeap)
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, idx, node))
        # [4, 2, ]
        # dummy -> 1 -> 3
        dummy = ListNode(-1)
        curr = dummy
        while minHeap:
            val, idx, node = heapq.heappop(minHeap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(minHeap, (node.next.val, idx, node.next))
        return dummy.next  

