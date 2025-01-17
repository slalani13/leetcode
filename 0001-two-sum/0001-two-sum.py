class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap = defaultdict(int)

        # for i in range(len(nums)):
        #     key = target - nums[i]
        #     if key in hashmap and hashmap[key] != i:
        #         return [i, hashmap[key]]
        #     hashmap[nums[i]] = i
        

        # recursive solution O(n) time and space
        def rec(i, hashmap, target):
            key = target - nums[i]
            if key in hashmap and hashmap[key] != i:
                return [i, hashmap[key]]
            hashmap[nums[i]] = i
            return rec(i+1, hashmap, target)

        return rec(0, {}, target)