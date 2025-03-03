class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        for num, freq in counter.items():
            buckets[freq].append(num)
        # print(buckets)
        res = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                # print(res)
                if len(res) == k:
                    return res