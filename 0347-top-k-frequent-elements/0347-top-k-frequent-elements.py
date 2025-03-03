class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        heapq.heapify(heap)
        counter = Counter(nums)
        # print(counter)
        for num, freq in counter.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        # print(heap)
        res = []
        for tup in heap:
            res.append(tup[1])
        return res