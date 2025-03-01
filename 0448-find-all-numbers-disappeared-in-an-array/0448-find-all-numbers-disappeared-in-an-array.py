class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output = []
        sset = set(nums)
        n = len(nums)
        for i in range(1, n+1):
            if i not in sset:
                output.append(i)
        return output