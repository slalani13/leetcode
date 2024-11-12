class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[0], nums[1], nums[2])

        n = len(nums)
        first = []
        last = []
        for i in range(n):
            if i != 0:
                last.append(nums[i])
            if i != n-1:
                first.append(nums[i])
        
        dp1 = [-1] * (n-1)
        dp2 = [-1] * (n-1)
        dp1[0], dp1[1] = first[0], max(first[0], first[1])
        dp2[0], dp2[1]= last[0], max(last[0], last[1])
        for i in range(2, n-1):
            dp1[i] = max(dp1[i-1], first[i] + dp1[i-2])
            dp2[i] = max(dp2[i-1], last[i] + dp2[i-2])
        
        return max(dp1[-1], dp2[-1])


