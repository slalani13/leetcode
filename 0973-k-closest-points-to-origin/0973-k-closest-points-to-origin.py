import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for p in points:
            x, y = p
            dist = math.sqrt(x**2 + y**2)
            distances.append([-dist, [x, y]])
        heapq.heapify(distances)
        while len(distances) > k:
            heapq.heappop(distances)
        res = [dist[1] for dist in distances]
        return res
