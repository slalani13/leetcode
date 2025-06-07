class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixSum = [0] * len(nums)
        self.prefixSum[0] = nums[0]
        for i in range(1, len(nums)):
            self.prefixSum[i] = self.nums[i] + self.prefixSum[i-1]

    def sumRange(self, left: int, right: int) -> int:
        # nums = [-2, 0, 3, -5, 2, -1]
        # sums = [-2, -2, 1, -4, -2, -3]
        # [0, 2] = prefixSums[0:2+1]
        # [2, 5] = 3-5+2-1 = -1 -> prefixSums[5] - prefixSums[2-1] = -3 - (-2) = -1
        if left == 0:
            return self.prefixSum[right]
        return self.prefixSum[right] - self.prefixSum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)