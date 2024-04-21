class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        cp = 0
        buyPrice = prices[0]
        for i in range (1, len(prices)):
            if prices[i] <= buyPrice:
                buyPrice = prices[i]
            else:
                cp = prices[i] - buyPrice
                if cp > mp:
                    mp = cp
        return mp