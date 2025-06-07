class Solution:
    def trap(self, height: List[int]) -> int:
        # create a max left and right array
        # array= [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        # left = [0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3]
        # right =[3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 0]
        # use the left and right walls to determine how much water can be held by checking min wall height
        n = len(height)
        leftMax, rightMax = 0, 0
        left = [0] * n
        right = [0] * n
        i, j = 0, n-1
        while i <= n and j >= 0:
            left[i] = leftMax
            leftMax = max(leftMax, height[i])
            i += 1
            right[j] = rightMax
            rightMax = max(rightMax, height[j])
            j -= 1
        
        res = 0
        for i in range(n):
            res += max(min(left[i], right[i]) - height[i], 0)
        return res
        
