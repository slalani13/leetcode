class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # use heaps to sort in n log n
        # heapify is O(n), push k points onto heap and repeat for n points
        arr = []
        for x1, y1 in points:
            dist = math.sqrt(x1**2 + y1**2)
            heapq.heappush(arr, (-dist, x1, y1))
            while len(arr) > k:
                heapq.heappop(arr)
        # print(arr)
        # while len(arr) > k:
        #     heapq.heappop(arr)
        res = [[x1, x2] for dist, x1, x2 in arr]
        return res
