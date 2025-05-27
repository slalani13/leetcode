class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = defaultdict(int)
        # map = [1:0, 2:1, 3:2, ]
        # [1,2,3,1] k=3
        for idx, num in enumerate(nums):
            if num in hashmap:
                i = hashmap[num]
                if abs(i-idx) <= k:
                    return True
            hashmap[num] = idx
        return False
