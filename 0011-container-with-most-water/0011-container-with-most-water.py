class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R = 0, len(height)-1
        maxArea = 0

        while L < R:
            width = R-L
            minHeight = min(height[L], height[R])
            area = width * minHeight
            maxArea = max(maxArea, area)
            if height[L] >= height[R]:
                R-=1
            else:
                L+=1
        return maxArea