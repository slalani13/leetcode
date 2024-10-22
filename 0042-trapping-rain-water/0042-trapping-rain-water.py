class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n
        maxLeft = 0
        maxRight = 0
        total = 0
        
        for i in range(n):
            j = -i - 1
            left[i] = maxLeft
            right[j] = maxRight
            maxLeft = max(maxLeft, height[i])
            maxRight = max(maxRight, height[j])
        
        for i in range(n):
            potential = min(left[i], right[i])
            total += max(0,potential-height[i])
        return total
