import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # heap = [8,7, 4, 2, 1, 1]
        for i in range(len(stones)):
            stones[i] *= -1
        heap = heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x == y:
                continue
            elif x < y:
                x = x-y
                heapq.heappush(stones, x)
            else:
                y = y-x
                heapq.heappush(stones, y)
        return stones[0]*-1 if stones else 0