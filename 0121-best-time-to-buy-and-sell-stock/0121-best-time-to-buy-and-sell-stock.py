class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]
        for p in prices:
            if p < minPrice:
                minPrice = p
            currentProfit = p - minPrice
            maxProfit = max(maxProfit, currentProfit)
        return maxProfit
