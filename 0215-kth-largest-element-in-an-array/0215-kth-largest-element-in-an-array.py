class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        heapq.heapify(min_heap)
        for i in range(len(nums)):
            if len(min_heap) < k:
                heapq.heappush(min_heap, nums[i])
            else:
                if nums[i] > min_heap[0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, nums[i])

        return min_heap[0]
            
            
