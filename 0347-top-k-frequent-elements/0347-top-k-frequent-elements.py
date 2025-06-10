class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create Counter and use heap to push each val, key onto heap, use maxHeap
        # n + logk*n = O(nlogk)
        freq = Counter(nums)
        # print(freq)
        minHeap = []
        for num, freq in freq.items():
            heapq.heappush(minHeap, (freq, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        res = []
        # print(minHeap)        
        while minHeap:
            freq, num = heapq.heappop(minHeap)
            res.append(num)
        return res

        