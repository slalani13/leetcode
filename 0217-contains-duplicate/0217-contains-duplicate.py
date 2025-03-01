class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sset = set()
        for n in nums:
            if n in sset:
                return True
            sset.add(n)
        return False