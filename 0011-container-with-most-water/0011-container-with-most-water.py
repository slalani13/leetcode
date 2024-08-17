class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        beg, end = 0, len(height)-1
        while beg < end:
            area = min(height[beg], height[end]) * (end-beg)
            maxArea = max(maxArea, area)
            if height[beg] < height[end]:
                beg += 1
            else:
                end -= 1
        return maxArea