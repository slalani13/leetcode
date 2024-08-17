class Solution:
    def trap(self, height: List[int]) -> int:
        # get left height and right height arrays
        L, R = [], deque()
        maxL = 0
        maxR = 0
        for i in range(len(height)):
            L.append(maxL)
            maxL = max(maxL, height[i])
        print(L)
        for i in range(len(height)-1, -1, -1):
            R.appendleft(maxR)
            maxR = max(maxR, height[i])
        print(R)
        # get sum
        total = 0
        for i in range(len(height)):
            water = min(L[i], R[i]) - height[i]
            if water > 0:
                total += water
        return total