import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for i in range(len(stones)):
            heapq.heappush(maxHeap, -stones[i])
        while len(maxHeap) > 1:
            first = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)
            if first != second:
                heapq.heappush(maxHeap, first - second)
        return -maxHeap[0] if len(maxHeap) > 0 else 0

