import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            distance = (p[0]*p[0] + p[1]*p[1])
            heapq.heappush(heap, (-distance, p))
            if len(heap) > k:
                heapq.heappop(heap)
        return [p for (distance, p) in heap]
