class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)

        def finish(k):
            hours = 0
            for banana in piles:
                hours += ceil(banana/k)
            if hours <= h:
                return True
            else:
                return False
        
        ans = R
        while L < R:
            mid = L+(R-L) // 2
            if finish(mid):
                ans = mid
                R = mid
            else:
                L = mid + 1
        return ans