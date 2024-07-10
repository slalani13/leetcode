class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        p = len(piles)
        low, high = 1, max(piles)
        res = high
        while low <= high:
            mid = low + ((high - low) // 2)
            total_hours = 0
            for i in range(p):
                total_hours += math.ceil(piles[i] / mid)
            if total_hours <= h:
                res = min(mid, res)
                high = mid-1
            else:
                low = mid+1
        return res


