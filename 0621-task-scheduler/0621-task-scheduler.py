class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # [AAABBCC] n = 2, m = len(tasks)
        # create count map O(m)
        # add to heap to get highest frequency value O(m)
        # for each timeframe, pop from heap reduce value and keep popping O(n*m*logm)
        # use q to add back into heap
        countMap = {}
        for task in tasks:
            if task in countMap:
                countMap[task] += 1
            else:
                countMap[task] = 1
        maxHeap = []
        for freq in countMap.values():
            maxHeap.append(-freq)
        heapq.heapify(maxHeap)
        q = deque()
        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap: # [-3, -3]
                freq = heapq.heappop(maxHeap)
                freq += 1
                if freq < 0:
                    q.append((freq, n+time))
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

