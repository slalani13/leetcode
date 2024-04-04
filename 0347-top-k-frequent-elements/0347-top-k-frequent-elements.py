class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # edge cases, no list
        if not nums:
            return []
        output = []
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        res_arr = [[] for _ in range(len(nums))]
        print(res_arr)
        for key, value in count.items():
            res_arr[value - 1].append(key)
        for i in range(len(nums)-1,-1,-1):
            if len(res_arr[i])>0 and k>0:
                for value in res_arr[i]:
                    if k>0:
                        output.append(value)
                        k-=1
        return output


        