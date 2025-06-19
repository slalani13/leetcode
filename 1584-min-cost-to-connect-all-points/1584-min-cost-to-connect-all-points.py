class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # connect all points, get min cost, MST, use Prims
        # seen set and minHeap
        # add starting node to minHeap
        # pop node and add all edges from node to minHeap, add node to seen, ignore if not seen
        # update and return cost
        # visit all nodes
        minHeap = [(0, 0)] # distance to node 0, index of node
        seen = set()
        n = len(points)
        cost = 0
        while len(seen) < n:
            dist, idx = heapq.heappop(minHeap)
            if idx in seen:
                continue
            seen.add(idx)
            cost += dist
            xi, yi = points[idx]
            for i in range(n):
                if i not in seen:
                    xj, yj = points[i]
                    new_dist = abs(xi-xj) + abs(yi-yj)
                    heapq.heappush(minHeap, (new_dist, i))
        return cost