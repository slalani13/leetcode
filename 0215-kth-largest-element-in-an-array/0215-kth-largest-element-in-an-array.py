class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # arr of size k, we want the kth-largest element which would be a minheap
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            while len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap[0]