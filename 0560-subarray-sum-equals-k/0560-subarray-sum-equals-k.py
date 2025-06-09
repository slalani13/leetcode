class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # nums = [1, 2, 3, 4], prefix=10, count=1, k=2
        # map: {0:1; 1:1; 3: 1; 6:1; 10: 1}
        # save prefixes in an array and check if prefix - k exists in arr
        # covers all subarray sums so far, each subarray is different, no duplicates
        prefix=0
        count=0
        prefix_map = defaultdict(int)
        prefix_map[0] = 1 # prefix : freq
        for i in range(len(nums)):
            prefix += nums[i]
            count += prefix_map[prefix-k]
            prefix_map[prefix] += 1
        return count
