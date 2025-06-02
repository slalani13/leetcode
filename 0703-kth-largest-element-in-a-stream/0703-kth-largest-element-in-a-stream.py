class KthLargest:

    def __init__(self, k: int, nums: List[int]): # 
        self.minHeap = nums
        heapq.heapify(self.minHeap) # O(n)
        while len(self.minHeap) > k: # initializes a minheap with k nodes
            heapq.heappop(self.minHeap) # (logn * (n-k))
        self.k = k

    def add(self, val: int) -> int: # O(1)
        heapq.heappush(self.minHeap, val) # size k + 1
        while len(self.minHeap) > self.k: 
            heapq.heappop(self.minHeap) # size k
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)